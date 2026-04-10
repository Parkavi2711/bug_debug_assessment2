# Assessment 2 — Multi-Agent Bug Debugging Workflow

A Python-based multi-agent system that automates the bug debugging lifecycle — from triage and log analysis through reproduction, fix planning, and critical review.

## Overview

The project simulates a structured debugging pipeline using five specialised agents that collaborate sequentially to analyse a bug report, inspect logs, reproduce the crash, propose a fix, and review the entire analysis for gaps.

**Bug under investigation:** Application crashes when processing input payloads that exceed a fixed-size buffer (IndexError due to missing input-size validation).

## Project Structure

```
assessment_2_bug_debug/
├── main.py
├── agents/
│   ├── triage_agent.py
│   ├── log_analyst_agent.py
│   ├── reproduction_agent.py
│   ├── fix_planner_agent.py
│   └── critic_agent.py
├── tools/
│   └── executor.py
├── inputs/
│   ├── bug_report.md
│   └── logs.txt
├── repro/
│   └── repro_script.py
└── output/
    └── final_report.json
```

## Agents

| Agent | Role |
|---|---|
| **TriageAgent** | Reads the bug report, extracts symptoms, identifies expected vs actual behaviour, and assigns severity. |
| **LogAnalystAgent** | Parses application logs to extract error types, messages, stack traces, and file references. |
| **ReproductionAgent** | Generates a minimal script that triggers the bug and executes it to confirm the crash. |
| **FixPlannerAgent** | Analyses outputs from prior agents to determine the root cause, propose a patch plan, and define a validation strategy. |
| **CriticAgent** | Reviews all previous outputs, challenges assumptions, and surfaces open questions or edge cases. |

## How It Works

1. **Triage** — Reads `inputs/bug_report.md` and extracts key symptoms and severity.
2. **Log Analysis** — Parses `inputs/logs.txt` to find error signatures and stack traces.
3. **Reproduction** — Writes a minimal repro script to `repro/repro_script.py` and executes it to confirm the crash.
4. **Fix Planning** — Synthesises findings into a root cause, patch plan, and validation strategy.
5. **Critic Review** — Evaluates all agent outputs for completeness and flags open questions.
6. **Report** — Writes the consolidated results to `output/final_report.json`.

## Setup & Usage

### Prerequisites

- Python 3.10+

### Steps

```bash
# 1. Create and activate a virtual environment
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1
# Linux/macOS
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the workflow
python main.py
```

### Output

On completion the script prints a confirmation and writes `output/final_report.json` containing the structured results from all five agents.

## Inputs

- **`inputs/bug_report.md`** — Describes a crash triggered by large input payloads, including expected/actual behaviour and environment details.
- **`inputs/logs.txt`** — Contains timestamped application logs showing a `ValueError` / `IndexError` when input exceeds the allocated buffer capacity.