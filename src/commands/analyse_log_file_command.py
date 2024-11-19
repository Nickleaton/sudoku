"""AnalyseLogFileCommand."""
from pathlib import Path
from tempfile import NamedTemporaryFile

import orloge

from src.commands.command import CommandException, Command
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

    def precondition_check(self, problem: Problem):
        """Check if the necessary conditions are met before executing the command.

        Args:
            problem (Problem): The problem instance to check for preconditions.

        Raises:
            CommandException: If no solver is set in the problem or if the target key already exists in the problem.
        """
        if problem.solver is None:
            raise CommandException("No solver has been set.")
        if self.target in problem:
            raise CommandException(f"{self.__class__.__name__} - {self.target} already in problem")

    def execute(self, problem: Problem):
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

    def __repr__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representation of the AnalyseLogFileCommand instance, showing log and target keys.
        """
        return f"ExtractAnswerCommand({self.log!r}, {self.target!r})"
