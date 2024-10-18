from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Dict

import orloge

from src.commands.command import CommandException, Command
from src.commands.problem import Problem


class AnalyseLogFileCommand(Command):
    """
    Extract the answer from the solver's results.
    """

    def __init__(self, log: str = 'log', target: str = 'log_analysis'):
        super().__init__()
        self.log: str = log
        self.target: str = target

    def precondition_check(self, problem: Problem):
        if problem.solver is None:
            raise CommandException("No solver has been set.")
        if self.target in problem:
            raise CommandException(f"{self.__class__.__name__} - {self.target} already in problem")

    def execute(self, problem: Problem):
        log_data: Dict= problem[self.log]
        application_name: str = log_data['application_name']
        log_contents: str = log_data['log_contents']
        with NamedTemporaryFile(mode='w+', delete=False) as temp_log_file:
            log_path: Path = Path(temp_log_file.name)
            temp_log_file.write(log_contents)
        try:
            # Pass the temp file to the analysis
            problem[self.target] = orloge.get_info_solver(log_path.name, application_name)
        finally:
            # Delete the temp file`
            log_path.unlink(missing_ok=True)

    def __repr__(self) -> str:
        return f"ExtractAnswerCommand({self.log!r}, {self.target!r})"
