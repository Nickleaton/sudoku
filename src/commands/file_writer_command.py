"""FileWriterCommand."""
from pathlib import Path

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class FileWriterCommand(SimpleCommand):
    """Write output into start file_path."""

    def __init__(self, source: str, target: Path) -> None:
        """Initialize FileReaderCommand.

        Args:
            source (str): The name of the string number in problem to write to the target file
            target (Path): Name of the target file.
        """
        super().__init__()
        self.source: str = source
        self.target: Path = target

    def work(self, problem: Problem) -> None:
        """Write to start file_path.

        Args:
            problem (Problem): The problem to load the file_path and file_path name into.

        Raises:
            CommandException: If an error occurs while writing the file_path.
        """
        super().work(problem)
        if self.source not in problem:
            raise CommandException(f'FileWriterCommand requires {self.source} in problem.')
        if not isinstance(problem[self.source], str):
            raise CommandException('FileWriterCommand can only write strings.')
        target_file_path: Path = problem.output_directory / self.target
        try:
            with target_file_path.open(mode='w', encoding='utf-8') as file_handler:
                file_handler.write(problem[self.source])
        except Exception as exc:
            raise CommandException(f'Failed to write {target_file_path!s}: {exc}') from exc

    def __repr__(self) -> str:
        """Return a string representation of the command.

        Returns:
            str: The string representation of the command
        """
        return f'{self.__class__.__name__}({self.source!r}, {self.target!r})'
