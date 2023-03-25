""" Base class for simple commands"""
import logging
from pathlib import Path
from typing import Any

import oyaml as yaml

from src.commands.command import Command
from src.items.board import Board
from src.items.item import Item


class SimpleCommand(Command):

    def __init__(self, config_filename: Path):
        """ Create the simple command

        :param config_filename: name of the yaml file containing the puzzle
        """
        super().__init__()
        self.__dict__['output'] = {}
        self.config_filename = config_filename
        self.config = None
        self.board = None
        self.problem = None

    def __getattr__(self, key: str) -> Any:
        return self.output[key]

    def __setattr__(self, key: str, value: Any):
        self.output[key] = value

    def load_config(self) -> None:
        """Load the config from the config_filename"""
        logging.info(f"Loading config from {self.config_filename}")
        with open(self.config_filename, 'r', encoding='utf-8') as file:
            self.config = yaml.load(file, yaml.SafeLoader)

    def create_board(self):
        """ Create the board"""
        logging.info("Creating board")
        self.board = Board.create('Board', self.config)

    def create_problem(self):
        """Create the problem"""
        logging.info("Creating problem")
        self.problem = Item.create(self.board, {'Constraints': self.config['Constraints']})

    def execute(self) -> None:
        """Process the command
        1. Load the config
        2. Create the board
        3. Construct the problem
        """
        self.load_config()
        self.create_board()
        self.create_problem()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.config_filename}')"
