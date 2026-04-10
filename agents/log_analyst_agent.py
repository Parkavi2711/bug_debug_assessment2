class LogAnalystAgent:
    """
    Log Analyst Agent

    Responsibilities:
    - Parse application logs
    - Extract error signatures and stack traces
    - Identify high-confidence failure evidence
    """

    def __init__(self, logs_path: str):
        self.logs_path = logs_path

    def _read_logs(self) -> str:
        with open(self.logs_path, "r") as f:
            return f.read()

    def run(self) -> dict:
        logs = self._read_logs()
        lines = logs.splitlines()

        error_lines = []
        stack_trace = []
        error_type = None
        error_message = None
        file_reference = None

        for line in lines:
            # Capture error lines
            if "ERROR" in line or "Traceback" in line or line.strip().startswith("File"):
                error_lines.append(line)

            # Extract error type and message
            if "IndexError" in line or "ValueError" in line:
                error_type = line.strip().split(":")[0]
                error_message = line.strip()

            # Extract file and line number
            if "File" in line and "line" in line:
                file_reference = line.strip()

        # Build stack trace text
        if error_lines:
            stack_trace = error_lines

        return {
            "agent": "LogAnalyst",
            "analysis": {
                "error_type": error_type,
                "error_message": error_message,
                "file_reference": file_reference,
                "stack_trace_excerpt": stack_trace
            }
        }
