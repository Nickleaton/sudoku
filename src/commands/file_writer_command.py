"""FileWriterCommand."""
from pathlib import Path

from src.commands.command import CommandException
from src.commands.key_type import KeyType
from src.commands.parameter_value_type import ParameterValueType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class FileWriterCommand(SimpleCommand):
    """Write output into a file."""

    def __init__(self,
                 file_name: str = 'file_name',
                 source: str = 'file_data',
                 file_path: Path = Path('test.txt')
                 ):
        """Initialize FileReaderCommand.

        Args:
            source (str): Name of the text to write to the file
            file_name (str): The name of the variable to store the name of the file in the problem.
            file_path (Path): Path to the template file.
        """
        super().__init__()
        self.source: str = source
        self.file_name: str = file_name
        self.file_path: Path = file_path
        self.parameters = [
            ParameterValueType(file_name, self.file_path, Path)
        ]
        self.input_types: list[KeyType] = [
            KeyType(self.source, str)
        ]

    def work(self, problem: Problem) -> None:
        """Write to a file.

        Args:
            problem (Problem): The problem to load the file and file name into.

        Raises:
            CommandException: If an error occurs while writing the file.
        """
        super().work(problem)
        try:
            with self.file_path.open(mode='w', encoding='utf-8') as file:
                if isinstance(problem[self.source], str):
                    file.write(problem[self.source])
                else:
                    raise CommandException("FileWriterCommand can only write strings.")
        except Exception as exc:
            raise CommandException(f"Failed to write {self.file_path!s}: {exc}") from exc
