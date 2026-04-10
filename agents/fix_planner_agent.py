class FixPlannerAgent:
    """
    Fix Planner Agent

    Responsibilities:
    - Identify the most likely root cause
    - Propose a patch plan
    - Define a validation strategy
    """

    def run(
        self,
        triage_output: dict,
        log_analysis_output: dict,
        reproduction_output: dict
    ) -> dict:
        reproduced = reproduction_output.get("reproduced", False)
        error_type = log_analysis_output["analysis"].get("error_type")

        # Root cause analysis
        root_cause = (
            "The application writes input data into a fixed-size buffer "
            "without validating input length, leading to an out-of-bounds write."
        )

        # Patch plan
        patch_plan = [
            "Add explicit input size validation before buffer write operations.",
            "Reject or truncate inputs that exceed buffer capacity.",
            "Add unit tests covering boundary and oversized inputs."
        ]

        # Validation plan
        validation_plan = [
            "Re-run the minimal reproduction script to confirm the crash no longer occurs.",
            "Add automated tests for maximum allowed input sizes.",
            "Perform regression testing on existing input scenarios."
        ]

        risks = [
            "Input truncation may impact downstream processing logic.",
            "Strict validation may change behavior for existing users."
        ]

        return {
            "agent": "FixPlanner",
            "analysis": {
                "reproduction_confirmed": reproduced,
                "error_type": error_type,
                "root_cause": root_cause,
                "patch_plan": patch_plan,
                "validation_plan": validation_plan,
                "risks": risks
            }
        }