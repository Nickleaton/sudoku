""" Load Config File """
import logging
from pathlib import Path

import oyaml as yaml
from pydotted import pydot

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.file_handling import is_readable_file


class LoadConfigCommand(SimpleCommand):

    def __init__(self, source: Path | str, target: str = 'config'):
        """
        Initialize LoadConfigCommand

        :param source: Path to the config file
        """
        super().__init__()
        self.source: Path = Path(source) if isinstance(source, str) else source
        self.target: str = target

    def precondition_check(self, problem: Problem) -> None:
        """
        Check the preconditions for the command.

        This method checks that the target attribute does not already exist in the
        problem's configuration and that the source file exists and is readable.

        :param problem: The problem to check
        :raises CommandException: If the preconditions are not met
        """
        if self.target in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.target} already exists')
        if not is_readable_file(self.source):
            raise CommandException(f'{self.__class__.__name__} - {self.source} does not exist or is not readable ')

    def execute(self, problem: Problem) -> None:

        """
        Load the configuration from the YAML file

        :return: None
        """
        super().execute(problem)
        logging.info(f"Loading config File {self.source}")
        with open(self.source, 'r', encoding='utf-8') as file:
            problem[self.target] = pydot(yaml.load(file, yaml.SafeLoader))

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}({repr(str(self.source))}, {repr(self.target)})"
