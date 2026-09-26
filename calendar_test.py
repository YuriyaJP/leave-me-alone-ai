from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import sqlite3

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

# --- Google Calendar ---
flow = InstalledAppFlow.from_client_secrets_file(
    "client_secret.json",
    SCOPES
)

credentials = flow.run_local_server(port=0)

service = build("calendar", "v3", credentials=credentials)

from datetime import datetime, timezone

now = datetime.now(timezone.utc).isoformat()

events_result = service.events().list(
    calendarId="primary",
    timeMin=now,
    maxResults=50,
    singleEvents=True,
    orderBy="startTime"
).execute()

events = events_result.get("items", [])

# --- SQLite ---
connection = sqlite3.connect("workload.db")
cursor = connection.cursor()

for event in events:
    event_id = event.get("id")
    title = event.get("summary", "(No title)")

    start = event["start"].get(
        "dateTime",
        event["start"].get("date")
    )

    end = event["end"].get(
        "dateTime",
        event["end"].get("date")
    )

    cursor.execute("""
        INSERT INTO calendar_events
        (event_id, title, start_time, end_time)
        VALUES (?, ?, ?, ?)
    """, (event_id, title, start, end))

connection.commit()
connection.close()

print(f"Saved {len(events)} calendar events to workload.db")