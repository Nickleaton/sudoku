"""FileReaderCommand."""
from pathlib import Path

from src.commands.command import CommandException
from src.commands.key_type import KeyType
from src.commands.parameter_value_type import ParameterValueType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class FileReaderCommand(SimpleCommand):
    """Load file into problem."""

    def __init__(self,
                 file_name: str = 'file_name',
                 target: str = 'file_data',
                 file_path: Path = Path('test.txt')
                 ):
        """Initialize FileReaderCommand.

        Args:
            target (str): The name of the variable to store the file contents in the problem
            file_name (str): The name of the variable to store the name of the file in the problem.
            file_path (Path): Path to the template file.
        """
        super().__init__()
        self.target: str = target
        self.file_name: str = file_name
        self.file_path: Path = file_path
        self.parameters = [
            ParameterValueType(file_name, self.file_path, Path)
        ]
        self.input_types: list[KeyType] = []
        self.output_types: list[KeyType] = [
            KeyType(self.target, str)
        ]

    def work(self, problem: Problem) -> None:
        """Load a file.

        Args:
            problem (Problem): The problem to load the file and file name into.

        Raises:
            CommandException: If an error occurs while loading the file.
        """
        super().work(problem)
        try:
            with self.file_path.open(mode='r', encoding='utf-8') as file:
                problem[self.target] = file.read()
        except Exception as exc:
            raise CommandException(f"Failed to load {self.source}: {exc}") from exc
