"""Load Config File."""
import logging
from pathlib import Path

import oyaml as yaml
from pydotted import pydot

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.file_handling import is_readable_file


class LoadConfigCommand(SimpleCommand):
    """Load Config into the problem."""

    def __init__(self, source: Path | str, target: str = 'config'):
        """Initialize LoadConfigCommand.

        Args:
            source (Path | str): Path to the config file.
            target (str): The name of the field in the problem to store the config. Defaults to 'config'.
        """
        super().__init__()
        self.source: Path = Path(source) if isinstance(source, str) else source
        self.target: str = target
        self.requirements = ['config']
        self.target = target

    def precondition_check(self, problem: Problem) -> None:
        """Check the preconditions for the command.

        This method checks that the target attribute does not already exist in the
        problem's configuration and that the source file exists and is readable.

        Args:
            problem (Problem): The problem to check.

        Raises:
            CommandException: If the preconditions are not met.
        """
        if not is_readable_file(self.source):
            raise CommandException(f'{self.__class__.__name__} - {self.source} does not exist or is not readable')
        if self.target in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.target} already exists')

    def execute(self, problem: Problem) -> None:
        """Load the configuration from the YAML file.

        Args:
            problem (Problem): The problem to load the config into.

        Raises:
            CommandException: If an error occurs while loading the config.
        """
        super().execute(problem)
        logging.info(f"Loading {self.source}")
        logging.info(f"Creating {self.target}")
        try:
            with self.source.open(mode='r', encoding='utf-8') as file:
                problem[self.target] = pydot(yaml.load(file, yaml.SafeLoader))
        except Exception as exc:
            raise CommandException(f"Failed to load {self.source}: {exc}") from exc

    def __repr__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}({str(self.source)!r}, {self.target!r})"
