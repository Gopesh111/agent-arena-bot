````markdown
# ThirdSight Prime

> An autonomous AI Agent built using **Google ADK**, **Gemini**, **MCP**, and **Traceloop** for the **Agent Arena** challenge at **Amadeus Agent Dev-Sprint: Build, Deploy & Battle**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4?style=for-the-badge&logo=google)
![Gemini](https://img.shields.io/badge/Gemini-AI-8E75FF?style=for-the-badge)
![MCP](https://img.shields.io/badge/MCP-Protocol-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

# Overview

**ThirdSight Prime** is an autonomous reasoning agent designed for the **Agent Arena** challenge.

Instead of simply generating responses, the agent follows a structured workflow:

- Understand the task
- Identify task type
- Plan the solution
- Use tools whenever required
- Review its own output
- Submit the final response autonomously

The project demonstrates how modern AI agents can combine **LLMs**, **tool calling**, **reasoning**, **evaluation**, and **observability** into a single workflow.

---

# Features

- Autonomous task solving
- Adaptive reasoning workflow
- Google Search integration
- Dynamic task classification
- Structured prompt generation
- Multi-turn conversations
- Live execution logging
- Score tracking
- Automatic task submission
- Traceloop observability
- MCP tool integration
- Google ADK powered

---

# Architecture

```text
                    ┌─────────────────────┐
                    │  Agent Arena (MCP)  │
                    └──────────┬──────────┘
                               │
                      Fetch Current Task
                               │
                               ▼
                    ┌─────────────────────┐
                    │ ThirdSight Prime    │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
     Task Classification   Planning      Google Search
             │
             ▼
      Adaptive Prompting
             │
             ▼
       Gemini Reasoning
             │
             ▼
       Self Evaluation
             │
             ▼
      Submit to Arena
             │
             ▼
        Score Tracking
```

---

# Tech Stack

| Category | Technology |
|----------|------------|
| Framework | Google ADK |
| LLM | Gemini |
| Agent Protocol | MCP |
| Language | Python |
| Observability | Traceloop |
| Telemetry | OpenTelemetry |
| Environment | python-dotenv |

---

# Workflow

```text
Register Agent
      │
      ▼
Fetch Task
      │
      ▼
Detect Task Type
      │
      ▼
Plan
      │
      ▼
Reason
      │
      ▼
Use Tools
      │
      ▼
Self Review
      │
      ▼
Submit
      │
      ▼
Track Score
      │
      ▼
Repeat
```

---

# Project Structure

```text
.
├── agent.py
├── prompts.py
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

---

# Supported Task Types

The prompt engine automatically detects different categories of tasks:

- Code Generation
- Debugging
- System Design
- Optimization
- Security
- Data Analysis
- Testing
- Explanation
- General Tasks

Each task receives a different reasoning strategy.

---

# Reasoning Pipeline

```text
Understand Task
      │
Extract Requirements
      │
Identify Edge Cases
      │
Plan Solution
      │
Generate Response
      │
Self Review
      │
Submit
```

---

# Observability

ThirdSight Prime supports execution tracing using:

- Traceloop
- OpenTelemetry
- Execution IDs
- Run IDs
- Agent IDs
- Task IDs

allowing every execution to be monitored from start to finish.

---

# Getting Started

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/agent-arena-bot.git

cd agent-arena-bot
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

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

# Dependencies

```text
google-adk
google-genai
fastmcp
traceloop-sdk
opentelemetry-api
opentelemetry-sdk
python-dotenv
litellm
```

---

# Key Learnings

Building production-ready AI agents is much more than calling an LLM.

This project explores concepts like:

- Agent Planning
- Tool Calling
- Reflection
- Evaluation
- Context Management
- Autonomous Decision Making
- Observability
- Multi-turn Execution

---

# Future Improvements

- Memory Integration
- Multi-Agent Collaboration
- Human Feedback Loop
- Better Evaluation Pipeline
- RAG Support
- Persistent Sessions
- Tool Routing
- Long-term Memory

---

# Acknowledgements

Built during **Agent Dev-Sprint: Build, Deploy & Battle** hosted by **Amadeus**.

Special thanks to the speakers, mentors, organizers, and the Google ADK ecosystem for making the event a great hands-on learning experience.

---



---


````
