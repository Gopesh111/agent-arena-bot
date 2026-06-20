# ThirdSight Prime

> An autonomous AI Agent built using **Google ADK**, **Gemini**, **MCP**, and **Traceloop** for the **Agent Arena** challenge at **Amadeus Agent Dev-Sprint: Build, Deploy & Battle**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4?style=for-the-badge&logo=google)
![Gemini](https://img.shields.io/badge/Gemini-AI-8E75FF?style=for-the-badge)
![MCP](https://img.shields.io/badge/MCP-Protocol-success?style=for-the-badge)

---

## Overview

ThirdSight Prime is an autonomous reasoning agent built for the **Agent Arena** challenge. It can analyze tasks, generate structured solutions, use external tools, and submit responses autonomously.

---

## Features

- Autonomous task execution
- Dynamic task classification
- Adaptive prompt generation
- Multi-turn reasoning
- MCP integration
- Google Search support
- Traceloop observability
- Automatic task submission

---

## Architecture

```
Agent Arena
      │
      ▼
ThirdSight Prime
      │
      ├── Task Classification
      ├── Planning
      ├── Gemini Reasoning
      ├── Tool Calling
      ├── Self Review
      └── Submission
```

---

## Tech Stack

- Python
- Google ADK
- Gemini
- MCP
- Traceloop
- OpenTelemetry

---

## Project Structure

```
.
├── agent.py
├── prompts.py
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Gopesh111/agent-arena-bot.git
cd agent-arena-bot
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
ID_TOKEN=YOUR_ID_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
TRACELOOP_API_KEY=YOUR_TRACELOOP_API_KEY
```

---

## Run

```bash
python agent.py
```

---

## Workflow

```text
Start
  │
  ▼
Register Agent
  │
  ▼
Fetch Task
  │
  ▼
Classify Task
  │
  ▼
Plan
  │
  ▼
Reason
  │
  ▼
Tool Calling
  │
  ▼
Self Review
  │
  ▼
Submit
  │
  ▼
Next Task
```

---

## Future Improvements

- Long-term memory
- Multi-agent collaboration
- Better evaluation pipeline
- RAG integration
- Persistent sessions

---

## Acknowledgements

Built during **Agent Dev-Sprint: Build, Deploy & Battle** hosted by **Amadeus**.

