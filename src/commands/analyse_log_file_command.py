"""AnalyseLogFileCommand."""
from pathlib import Path
from tempfile import NamedTemporaryFile

import orloge

from src.commands.command import Command
from src.commands.key_type import KeyType
from src.commands.problem import Problem


class AnalyseLogFileCommand(Command):
    """Command to analyze the solver's log file and extract relevant information."""

    def __init__(self, log: str = 'log', target: str = 'log_analysis'):
        """Initialize the AnalyseLogFileCommand.

        Args:
            log (str): The key in the problem where log data is stored. Defaults to 'log'.
            target (str): The key in the problem to store the analysis result. Defaults to 'log_analysis'.
        """
        super().__init__()
        self.log: str = log
        self.target: str = target

        self.inputs: list[KeyType] = [
            KeyType(log, str)
        ]
        self.outputs: list[KeyType] = [
            KeyType(target, str)
        ]

    def work(self, problem: Problem) -> None:
        """Execute the command to analyze the solver's log file.

        Args:
            problem (Problem): The problem instance containing the log data.

        Returns:
            None
        """
        log_data: dict = problem[self.log]
        application_name: str = log_data['application_name']
        log_contents: str = log_data['log_contents']
        with NamedTemporaryFile(mode='w+', delete=False) as temp_log_file:
            log_path: Path = Path(temp_log_file.name)
            temp_log_file.write(log_contents)
        try:
            # Pass the temp file to the analysis
            problem[self.target] = orloge.get_info_solver(log_path.name, application_name)
        finally:
            # Delete the temp file
            log_path.unlink(missing_ok=True)
