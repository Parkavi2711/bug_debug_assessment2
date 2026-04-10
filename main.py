import json

from agents.triage_agent import TriageAgent
from agents.log_analyst_agent import LogAnalystAgent
from agents.reproduction_agent import ReproductionAgent
from agents.fix_planner_agent import FixPlannerAgent
from agents.critic_agent import CriticAgent


def run_debugging_workflow():
    # Initialize agents
    triage_agent = TriageAgent("inputs/bug_report.md")
    log_agent = LogAnalystAgent("inputs/logs.txt")
    reproduction_agent = ReproductionAgent("repro/repro_script.py")
    fix_planner_agent = FixPlannerAgent()
    critic_agent = CriticAgent()

  
    triage_output = triage_agent.run()

    log_analysis_output = log_agent.run()

    
    reproduction_output = reproduction_agent.run()

   
    fix_plan_output = fix_planner_agent.run(
        triage_output,
        log_analysis_output,
        reproduction_output
    )

   
    critic_output = critic_agent.run(
        triage_output,
        log_analysis_output,
        reproduction_output,
        fix_plan_output
    )

  
    final_report = {
        "bug_summary": triage_output,
        "log_evidence": log_analysis_output,
        "reproduction": reproduction_output,
        "fix_plan": fix_plan_output,
        "critic_review": critic_output
    }

    return final_report


if __name__ == "__main__":
    report = run_debugging_workflow()

    # Save output to JSON file
    with open("output/final_report.json", "w") as f:
        json.dump(report, f, indent=2)

    # Print the SAME output to terminal
    print(json.dumps(report, indent=2))