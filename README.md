# Leave Me Alone AI

The idea: learn what matters to the user, monitor relevant information, and surface things that actually need attention. Ideally, this means spending a weekend away from email without wondering whether something important happened.

This is an early prototype.

## Current functionality

* **Google Calendar:** Fetches upcoming events through the Google Calendar API.
* **SQLite:** Stores calendar events and basic PC activity records locally.
* **Ollama:** Runs Llama 3.1 locally to interpret calendar data and produce a short summary.
* **PC activity tracking:** Records CPU usage by process at regular intervals. This is an experimental sensor, not a reliable measure of active work.

## Tech stack

| Component         | Technology          | Purpose                               |
| ----------------- | ------------------- | ------------------------------------- |
| Language          | Python              | Application logic and data processing |
| Calendar          | Google Calendar API | Retrieve upcoming events              |
| Database          | SQLite              | Local storage                         |
| LLM runtime       | Ollama              | Run the model locally                 |
| Model             | Llama 3.1           | Summarise and interpret data          |
| System monitoring | psutil              | Collect process-level CPU activity    |
| Environment       | Linux               | Development and execution             |

**Architecture**

```text
Google Calendar API
        |
        v
     Python  --------> SQLite
        |                 ^
        |                 |
        v                 |
   Ollama / Llama 3.1     |
                          |
PC activity tracker ------+

Gmail API: planned
```

Python handles data collection and processing. SQLite stores the collected records. Ollama runs the language model locally and generates summaries from the data supplied to it.

### Requirements

* Linux or another environment that supports Python and Ollama
* Python 3
* Ollama
* A downloaded Ollama model
* Google Calendar API credentials for calendar access

The current setup uses `llama3.1:latest`.

## Privacy and cost

The project is designed around local processing:

* Calendar data is retrieved through Google's API. (local files and credentials still need to be secured.)
* Collected records are stored in a local SQLite database.
* Llama runs through Ollama on the local machine.
* The current model-inference workflow does not require a hosted LLM API.


**Software cost so far: $0.**


## Roadmap

1. **Improve activity measurement:** distinguish active use from background CPU activity and develop more defensible workload indicators.
2. **Add Gmail:** retrieve messages and build a local representation suitable for prioritisation.
3. **Define priority rules:** let the user specify what can wait, what can be handled, and what warrants interruption.
4. **Add feedback:** use corrections and explicit instructions to improve future prioritisation.
5. **Build an interface:** replace terminal-only interaction with a simple personal assistant UI.
6. **Add weekend mode:** monitor for relevant events and notify the user only when defined conditions are met.
7. **Evaluate reliability:** test missed urgent items, unnecessary interruptions, incorrect classifications, and the system's explanations before trusting it with real decisions.

## The intended outcome is less mental overhead: fewer unnecessary checks, clearer priorities, and more confidence when disconnecting.

> I'm offline. Interrupt me only if it matters.
