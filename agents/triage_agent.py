class TriageAgent:
    """
    Triage Agent

    Responsibilities:
    - Read the bug report
    - Extract key symptoms
    - Identify expected vs actual behavior
    - Estimate severity
    """

    def __init__(self, bug_report_path: str):
        self.bug_report_path = bug_report_path

    def _read_bug_report(self) -> str:
        with open(self.bug_report_path, "r") as f:
            return f.read()

    def run(self) -> dict:
        report = self._read_bug_report()

        # Basic symptom extraction (deterministic)
        symptoms = []
        if "crash" in report.lower():
            symptoms.append("Application crash observed")

        if "large input" in report.lower():
            symptoms.append("Failure correlated with large input size")

        expected_behavior = (
            "Application should validate input size and handle large inputs gracefully"
        )

        actual_behavior = (
            "Application crashes when processing large input payloads"
        )

        severity = "High"

        return {
            "agent": "Triage",
            "summary": {
                "symptoms": symptoms,
                "expected_behavior": expected_behavior,
                "actual_behavior": actual_behavior,
                "severity": severity
            }
        }