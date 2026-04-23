# 🚀 LeadFlow Engine API

Event-driven backend for lead tracking, process automation, and workflow management

---

## 🧠 Overview

LeadFlow Engine API is a production-ready backend system designed to manage leads, business processes, and event-based workflows.

Unlike traditional systems that only store the current state, this system records every action as an event — enabling full visibility, automation, and scalability.

---

## 💼 Real-World Use Cases

* Lead generation systems (scraping, outreach, pipelines)
* CRM backends
* Automation workflows (follow-ups, status tracking)
* AI / agent-based processing systems
* Business process tracking & analytics

---

## 🔥 Key Features

* ✅ Client management
* ✅ Process-based workflow tracking
* ✅ Event-driven architecture (full history)
* ✅ Automatic state updates from events
* ✅ Aggregated endpoint (full process view)
* ✅ Clean and scalable backend structure

---

## ⚙️ Architecture

The system follows a clean layered architecture:

```
API (FastAPI)
↓
Schemas (Pydantic validation)
↓
Services (business logic)
↓
Repositories (data access)
↓
Database (MySQL)
```

---

## 🔄 Event-Driven Core

Instead of directly updating state:

```python
status = "contacted"
```

This system works with events:

```
Event: contacted → updates process status
Event: follow_up → updates process status
Event: closed → updates process status
```

### Benefits:

* Full history tracking
* Audit logs
* Automation-ready workflows
* Better scalability

---

## 🧱 Data Model

* **Clients** → companies / entities
* **Processes** → leads, workflows, pipelines
* **Process Events** → actions, changes, history

---

## 🛠 Tech Stack

* FastAPI
* SQLAlchemy
* MySQL
* Pydantic
* Uvicorn

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/JCarlosWolf/leadflow-engine-api.git
cd leadflow-engine-api
```

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```
PROJECT_NAME=LeadFlow Engine API
API_V1_STR=/api/leadflow

DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=leadflow_db
```

### 5. Initialize database

```python
from app.db.init_db import init_db
init_db()
```

### 6. Run the server

```bash
python -m uvicorn app.main:app --reload
```

### 7. API Documentation

Open in browser:

```
http://localhost:8000/docs
```

---

## 🧪 Example Workflow

1. Create a client
2. Create a process (lead)
3. Add events:

```json
{
  "process_id": 1,
  "event_type": "contacted",
  "description": "Email sent"
}
```

### Result:

* Event is stored
* Process status updates automatically
* Full history is preserved

---

## 📡 Key Endpoint

### Full Process View

```
GET /api/leadflow/processes/{process_id}/full
```

Returns:

```json
{
  "process": {...},
  "client": {...},
  "events": [...]
}
```

👉 Single endpoint to retrieve full context

---

## 🚀 Why This Matters

Most systems:

* overwrite state
* lose history
* are hard to automate

LeadFlow Engine:

* tracks every action
* preserves full history
* enables automation
* scales with complexity

---

## 💡 Future Improvements

* Authentication & authorization
* Webhooks / automation triggers
* Status validation rules
* Frontend dashboard
* Integration with scraping systems

---

## 💼 Business Value

This project demonstrates:

* Backend system design
* Clean architecture
* Real-world problem solving
* Scalable API development

---

## 📬 Contact

If you're interested in using or adapting this system:

👉 Open an issue or connect via GitHub

---

## ⚡ Summary

LeadFlow Engine API is not just a CRUD backend —
it's a scalable, event-driven system for managing leads and workflows in real environments.


