import sqlite3
import time
from datetime import datetime

import psutil


def get_top_processes(limit=10):
    processes = []

    for process in psutil.process_iter(["name", "cpu_percent"]):
        try:
            name = process.info["name"]
            cpu = process.info["cpu_percent"]

            if name and cpu is not None:
                processes.append((name, cpu))

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes.sort(key=lambda x: x[1], reverse=True)

    return processes[:limit]


def save_activity(application, cpu_percent):
    connection = sqlite3.connect("workload.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO app_activity
        (timestamp, application, cpu_percent)
        VALUES (?, ?, ?)
        """,
        (
            datetime.now().isoformat(),
            application,
            cpu_percent,
        ),
    )

    connection.commit()
    connection.close()


print("Activity tracker started.")

while True:
    processes = get_top_processes()

    for application, cpu_percent in processes:
        save_activity(application, cpu_percent)

    print(f"Recorded {len(processes)} processes.")

    time.sleep(10)