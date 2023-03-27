""" Load Config File """
import logging
from pathlib import Path

import oyaml as yaml

from src.commands.simple_command import SimpleCommand


class LoadConfigCommand(SimpleCommand):

    def __init__(self, config_filename: Path):
        super().__init__()
        self.config_filename = config_filename
        self.config = None

    def execute(self) -> None:
        """
        Load the config for a problem
        """
        logging.info(f"Loading config File {self.config_filename}")
        with open(self.config_filename, 'r', encoding='utf-8') as file:
            self.config = yaml.load(file, yaml.SafeLoader)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.config_filename}')"
