import sqlite3
import requests


connection = sqlite3.connect("workload.db")
cursor = connection.cursor()

events = cursor.execute("""
    SELECT title, start_time, end_time
    FROM calendar_events
    ORDER BY start_time
    LIMIT 10
""").fetchall()

connection.close()


calendar_text = "\n".join(
    f"- {title}: {start} → {end}"
    for title, start, end in events
)


prompt = f"""
You are a personal workload assistant.

Here are the user's upcoming calendar events:

{calendar_text}

Briefly summarise what their upcoming workload looks like.
Separate work-related commitments from personal events when possible.
Do not invent information that is not present.
"""


response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.1:latest",
        "prompt": prompt,
        "stream": False,
    },
)

print(response.json()["response"])