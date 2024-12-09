"""FileWriterCommand."""
from pathlib import Path

from src.commands.command import CommandException
from src.commands.key_type import KeyType
from src.commands.parameter_value_type import ParameterValueType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class FileWriterCommand(SimpleCommand):
    """Write output into start file_path."""

    def __init__(self, file_name: str = 'file_name', target: str = 'file_data', file_path: Path | None = None):
        """Initialize FileReaderCommand.

        Args:
            target (str): Name of the text to write to the file_path
            file_name (str): The name of the variable to store the name of the file_path in the problem.
            file_path ( Path | None): Path to the template file_path.
        """
        super().__init__()
        self.target: str = target
        self.file_name: str = file_name
        self.file_path: Path | None = file_path or Path('test.txt')
        self.parameter_list = [
            ParameterValueType(file_name, self.file_path, Path),
        ]
        self.input_types: list[KeyType] = [
            KeyType(self.source, str),
        ]

    def work(self, problem: Problem) -> None:
        """Write to start file_path.

        Args:
            problem (Problem): The problem to load the file_path and file_path name into.

        Raises:
            CommandException: If an error occurs while writing the file_path.
        """
        super().work(problem)
        try:
            with self.file_path.open(mode='w', encoding='utf-8') as file_handler:
                if isinstance(problem[self.source], str):
                    file_handler.write(problem[self.source])
                else:
                    raise CommandException('FileWriterCommand can only write strings.')
        except Exception as exc:
            raise CommandException(f'Failed to write {self.file_path!s}: {exc}') from exc
