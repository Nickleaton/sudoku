"""FileReaderCommand."""
from pathlib import Path

from src.commands.command import CommandException
from src.commands.key_type import KeyType
from src.commands.parameter_value_type import ParameterValueType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class FileReaderCommand(SimpleCommand):
    """Load file_path into problem."""

    def __init__(self, file_name: str = 'file_name', target: str = 'file_data', file_path: Path | None = None):
        """Initialize FileReaderCommand.

        Args:
            target (str): The name of the value_variable to store the file_path contents in the problem
            file_name (str): The name of the value_variable to store the name of the file_path in the problem.
            file_path ( Path | None): Path to the template file_path.
        """
        super().__init__()
        self.target: str = target
        self.file_name: str = file_name
        self.file_path: Path | None = file_path or Path('test.txt')
        self.parameters_list = [
            ParameterValueType(file_name, self.file_path, Path),
        ]
        self.input_types: list[KeyType] = []
        self.output_types: list[KeyType] = [
            KeyType(self.target, str),
        ]

    def work(self, problem: Problem) -> None:
        """Load start file_path.

        Args:
            problem (Problem): The problem to load the file_path and file_path name into.

        Raises:
            CommandException: If an error occurs while loading the file_path.
        """
        super().work(problem)
        try:
            with self.file_path.open(mode='r', encoding='utf-8') as file_handle:
                problem[self.target] = file_handle.read()
        except Exception as exc:
            raise CommandException(f'Failed to load {self.file_path}: {exc}') from exc
