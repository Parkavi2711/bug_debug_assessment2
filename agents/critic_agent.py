class CriticAgent:
    """
    Critic / Reviewer Agent

    Responsibilities:
    - Challenge assumptions made by other agents
    - Evaluate whether reproduction is truly minimal
    - Review fix plan for safety and completeness
    - Identify missing information or edge cases
    """

    def run(
        self,
        triage_output: dict,
        log_analysis_output: dict,
        reproduction_output: dict,
        fix_plan_output: dict
    ) -> dict:
        critiques = []
        open_questions = []

        # Critique reproduction
        if reproduction_output.get("reproduced"):
            critiques.append(
                "The reproduction successfully triggers the crash, "
                "but it assumes a fixed buffer size without verifying real production constraints."
            )
        else:
            critiques.append(
                "The reproduction did not consistently reproduce the crash. Confidence in the root cause is reduced."
            )

        # Critique root cause assumptions
        critiques.append(
            "The root cause assumes missing input validation is the sole issue. "
            "Other contributors such as memory reuse or concurrent access were not evaluated."
        )

        # Critique fix plan
        critiques.append(
            "The proposed fix plan is reasonable but may introduce behavior changes "
            "for clients relying on current lax validation."
        )

        # Identify open questions
        open_questions.append(
            "What is the intended maximum input size according to product requirements?"
        )
        open_questions.append(
            "Are there additional call paths where large input can bypass validation?"
        )
        open_questions.append(
            "Is input size enforcement consistent across all services handling this data?"
        )

        return {
            "agent": "Critic",
            "analysis": {
                "critiques": critiques,
                "open_questions": open_questions
            }
        }