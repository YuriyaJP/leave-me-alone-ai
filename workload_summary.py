import sqlite3

connection = sqlite3.connect("workload.db")
cursor = connection.cursor()

print("\n--- CALENDAR ---")

events = cursor.execute("""
    SELECT title, start_time, end_time
    FROM calendar_events
    ORDER BY start_time
    LIMIT 10
""").fetchall()

for title, start, end in events:
    print(f"{start} → {end}: {title}")


print("\n--- RECENT PC ACTIVITY ---")

activity = cursor.execute("""
    SELECT timestamp, application, cpu_percent
    FROM app_activity
    ORDER BY id DESC
    LIMIT 20
""").fetchall()

for timestamp, application, cpu in activity:
    print(f"{timestamp}: {application} ({cpu:.1f}% CPU)")


connection.close()