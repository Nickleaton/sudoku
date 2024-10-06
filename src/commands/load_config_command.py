""" Load Config File """
import logging
from pathlib import Path

import oyaml as yaml

from src.commands.command import Command, CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class LoadConfigCommand(SimpleCommand):

    def __init__(self, config_filename: Path):
        """
        Initialize LoadConfigCommand

        :param config_filename: Path to the config file
        """
        super().__init__()
        self.config_filename = config_filename

    def precondition_check(self, _: Problem) -> None:
        if not self.config_filename.exists():
            raise CommandException(f'{self.__class__.__name__} - {self.config_filename} does not exist')
        if not self.config_filename.is_file():
            raise CommandException(f'{self.__class__.__name__} - {self.config_filename} is not a file')


    def execute(self, problem: Problem) -> None:

        """
        Load the configuration from the YAML file

        :return: None
        """
        super().execute(problem)
        logging.info(f"Loading config File {self.config_filename}")
        with open(self.config_filename, 'r', encoding='utf-8') as file:
            problem.config = yaml.load(file, yaml.SafeLoader)

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}('{self.config_filename}')"
