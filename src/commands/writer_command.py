"""
Command that takes a command that produces an output string and writes it to a file.
"""
import logging
from pathlib import Path

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.file_handling import is_writeable_file


class WriterCommand(SimpleCommand):
    """Create a file from the output of a child command."""

    def __init__(self, source: str, target: Path | str):
        """Constructor.

        Args:
            source (str): The attribute of the problem to store the configuration in.
            target (Path | str): The name of the file to write the configuration to.
        """
        super().__init__()
        self.target: Path = Path(target) if isinstance(target, str) else target
        self.source: str = source

    def precondition_check(self, problem: Problem) -> None:
        """Check the preconditions for the command.

        This method checks that the source attribute specified by
        `source` exists in the problem and that the target file
        specified by `target` is writable.

        Args:
            problem (Problem): The problem to check.

        Raises:
            CommandException: If the preconditions are not met.
        """
        if self.source not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.source} not in problem')
        if not is_writeable_file(self.target):
            raise CommandException(f'{self.__class__.__name__} - {self.target} is not writable')

    def execute(self, problem: Problem) -> None:
        """Produce the file.

        This method performs the actual work of the command. It logs an info message
        indicating that the command is being processed and creates a new file in the
        specified location, storing it in the field specified by `target`.

        Args:
            problem (Problem): The problem to write the file of.

        Returns:
            None
        """
        super().execute(problem)
        if not self.target.parent.exists():
            logging.info(f"Creating directory {self.target.parent}")
            self.target.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating {self.target}")
        with open(self.target, 'w', encoding="utf-8") as f:
            f.write(problem[self.source])

    def __repr__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f'{self.__class__.__name__}({self.source!r}, {str(self.target)!r})'
