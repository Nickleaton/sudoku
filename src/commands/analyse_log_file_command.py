"""AnalyseLogFileCommand."""
import logging
from pathlib import Path
from tempfile import NamedTemporaryFile

import orloge

from src.commands.command import CommandException
from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class AnalyseLogFileCommand(SimpleCommand):
    """Command to analyze the solver's log file_path and extract relevant information."""

    def __init__(self, log: str = 'log', target: str = 'log_analysis'):
        """Initialize the AnalyseLogFileCommand.

        Args:
            log (str): The key in the problem where log line is stored. Defaults to 'log'.
            target (str): The key in the problem to store the analysis parsed_data. Defaults to 'log_analysis'.
        """
        super().__init__()
        self.log: str = log
        self.target: str = target

        self.inputs: list[KeyType] = [
            KeyType(log, str),
        ]
        self.outputs: list[KeyType] = [
            KeyType(target, str),
        ]

    @staticmethod
    def create_temp_log_file(log_contents: str) -> Path | None:
        """Create a temporary log file to store the log contents.

        Args:
            log_contents (str): The contents of the log file.

        Returns:
            Path | None: The path to the created temporary log file, or None if creation fails.
        """
        with NamedTemporaryFile(mode='w+', delete=False) as temp_log_file:
            log_path: Path = Path(temp_log_file.name)
            temp_log_file.write(log_contents)
        return log_path

    def analyze_log_file(self, problem: Problem, log_path: Path, application_name: str) -> None:
        """Analyze the log file and update the problem with the analysis parsed_data.

        Args:
            problem (Problem): The problem instance containing the log line.
            log_path (Path): The path to the log file.
            application_name (str): The application name from the log line.

        Raises:
            CommandException: If an error occurs while analyzing the log file.
        """
        try:
            problem[self.target] = orloge.get_info_solver(log_path.name, application_name)
        except Exception as exp:
            logging.error(f'Error analyzing the log file: {exp}', exc_info=True)
            raise CommandException(f'Failed to analyze the log file: {exp}')

    @staticmethod
    def cleanup_temp_log_file(log_path: Path) -> None:
        """Delete the temporary log file if it exists.

        Args:
            log_path (Path): The path to the temporary log file.
        """
        try:
            log_path.unlink(missing_ok=True)
        except Exception as exp:
            logging.error(f'Error deleting temporary log file: {exp}', exc_info=True)

    def work(self, problem: Problem) -> None:
        """Execute the command to analyze the solver's log file.

        Args:
            problem (Problem): The problem instance containing the log line.
        """
        log_data: dict = problem[self.log]
        application_name: str = log_data['application_name']
        log_contents: str = log_data['log_contents']

        log_path = self.create_temp_log_file(log_contents)
        if log_path:
            self.analyze_log_file(problem, log_path, application_name)
            self.cleanup_temp_log_file(log_path)
