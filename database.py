import sqlite3

connection = sqlite3.connect("workload.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS calendar_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id TEXT,
    title TEXT,
    start_time TEXT,
    end_time TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS app_activity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    application TEXT,
    cpu_percent REAL
)
""")

connection.commit()
connection.close()

print("Database created successfully.")