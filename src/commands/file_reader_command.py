"""FileReaderCommand."""
from pathlib import Path

from src.commands.command import CommandException
from src.commands.key_type import KeyType
from src.commands.parameter_value_type import ParameterValueType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class FileReaderCommand(SimpleCommand):
    """Command to load the contents of a file into a problem."""

    def __init__(self, file_name: str = 'file_name', target: str = 'file_data', file_path: Path | None = None):
        """Initialize FileReaderCommand.

        Args:
            file_name (str): The name of the variable to store the file name in the problem.
            target (str): The name of the variable to store the file contents in the problem.
            file_path (Path | None): Path to the file to read. Defaults to 'test.txt'.

        Raises:
            ValueError: If the provided file_path is not a valid file.
        """
        super().__init__()
        self.target: str = target
        self.file_name: str = file_name
        self.file_path: Path = file_path or Path('test.txt')

        if not self.file_path.is_file():
            raise ValueError(f"Provided file_path '{self.file_path}' is not a valid file.")

        self.parameters_list = [
            ParameterValueType(file_name, self.file_path, Path),
        ]
        self.input_types: list[KeyType] = []
        self.output_types: list[KeyType] = [
            KeyType(self.target, str),
        ]

    def work(self, problem: Problem) -> None:
        """Load file contents into the problem.

        Args:
            problem (Problem): The problem instance to load the file name and contents into.

        Raises:
            CommandException: If an error occurs while reading the file.
        """
        super().work(problem)
        try:
            with self.file_path.open(mode='r', encoding='utf-8') as file_handle:
                problem[self.target] = file_handle.read()
        except FileNotFoundError:
            raise CommandException(f'File not found: {self.file_path}')
        except Exception as exc:
            raise CommandException(f'Failed to load {self.file_path}: {exc}') from exc
