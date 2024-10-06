import logging
from pathlib import Path

import oyaml as yaml

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


def represent_none(self, _):
    return self.represent_scalar('tag:yaml.org,2002:null', '')


# Register the representer with the YAML dumper
yaml.add_representer(type(None), represent_none)


class ConfigWriterCommand(SimpleCommand):
    def __init__(self, config_filename: Path) -> None:
        """
        Initialize ConfigWriterCommand

        :param config_filename: Path to the config file
        """
        super().__init__()
        self.config_filename = config_filename

    def execute(self, problem: Problem) -> None:
        """
        Write the config file

        :return: None
        """
        if problem.config is None:
            raise CommandException('config')
        super().execute(problem)
        logging.info(f"Writing config File {self.config_filename}")
        with open(self.config_filename, 'w', encoding='utf-8') as file:
            yaml.dump(problem.config.todict(), file, default_style=None)

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}('{self.config_filename}')"
