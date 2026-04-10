# Assessment 2 — Multi-Agent Bug Debugging Workflow

A Python-based multi-agent system that automates the bug debugging lifecycle — from triage and log analysis through reproduction, fix planning, and critical review.

## Overview

The project simulates a structured debugging pipeline using five specialised agents that collaborate sequentially to analyse a bug report, inspect logs, reproduce the crash, propose a fix, and review the entire analysis for gaps.

**Bug under investigation:** Application crashes when processing input payloads that exceed a fixed-size buffer (IndexError due to missing input-size validation).

## Project Structure

```
assessment_2_bug_debug/
├── main.py                  # Orchestrates the full debugging workflow
├── agents/
│   ├── triage_agent.py      # Reads bug report, extracts symptoms & severity
│   ├── log_analyst_agent.py # Parses logs, extracts errors & stack traces
│   ├── reproduction_agent.py# Generates & runs a minimal repro script
│   ├── fix_planner_agent.py # Identifies root cause & proposes a patch plan
│   └── critic_agent.py      # Reviews all agent outputs for completeness
├── tools/
│   └── executor.py          # Executes Python scripts via subprocess
├── inputs/
│   ├── bug_report.md        # Sample bug report (large-input crash)
│   └── logs.txt             # Application logs with error traces
├── repro/
│   └── repro_script.py      # Generated reproduction script (written at runtime)
├── output/
│   └── final_report.json    # Consolidated JSON report (written at runtime)
└── 2_env/                   # Python virtual environment
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
# 1. Activate the virtual environment
# Windows
.\2_env\Scripts\Activate.ps1
# Linux/macOS
source 2_env/bin/activate

# 2. Run the workflow
python main.py
```

### Output

On completion the script prints a confirmation and writes `output/final_report.json` containing the structured results from all five agents.

## Inputs

- **`inputs/bug_report.md`** — Describes a crash triggered by large input payloads, including expected/actual behaviour and environment details.
- **`inputs/logs.txt`** — Contains timestamped application logs showing a `ValueError` / `IndexError` when input exceeds the allocated buffer capacity.