from tools.executor import run_python_script


class ReproductionAgent:
    """
    Reproduction Agent

    Responsibilities:
    - Generate a minimal reproducible script
    - Execute the script programmatically
    - Capture failure evidence
    """

    def __init__(self, repro_script_path: str):
        self.repro_script_path = repro_script_path

    def _write_repro_script(self):
        """
        Generate a minimal reproducible script that triggers the bug.
        """
        repro_code = """
def process_input(data):
    buffer = [0] * 1000  # fixed-size buffer
    for i in range(len(data)):
        buffer[i] = data[i]

# Trigger failure with large input
large_input = "A" * 1500
process_input(large_input)
"""

        with open(self.repro_script_path, "w") as f:
            f.write(repro_code)

    def run(self) -> dict:
        # Step 1: Write repro script
        self._write_repro_script()

        # Step 2: Execute repro script
        execution_result = run_python_script(self.repro_script_path)

        # Determine if crash reproduced
        reproduced = execution_result["exit_code"] != 0

        return {
            "agent": "Reproduction",
            "repro_script": self.repro_script_path,
            "reproduced": reproduced,
            "execution_output": execution_result
        }