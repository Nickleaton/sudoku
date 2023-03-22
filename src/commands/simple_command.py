""" Base class for simple commands"""
import logging
from pathlib import Path
from typing import Dict, Optional

import oyaml as yaml

from src.commands.command import Command
from src.items.board import Board
from src.items.item import Item
from src.items.solution import Solution


class SimpleCommand(Command):

    def __init__(self, config_filename: Path | str):
        """ Create the simple command

        :param config_filename: name of the yaml file containing the puzzle
        """
        super().__init__()
        if type(config_filename) == str:
            self.config_filename = Path(config_filename)
        else:
            self.config_filename = config_filename
        self.config: Optional[Dict] = None
        self.board: Optional[Board] = None
        self.problem: Optional[Item] = None
        self.solution: Optional[Solution] = None
        self.output: Optional[str] = None

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

    def process(self) -> None:
        """Process the command
        1. Load the config
        2. Create the board
        3. Construct the problem
        """
        self.load_config()
        self.create_board()
        self.create_problem()
        self.output = ""
    #
    # def write(self) -> None:
    #     """ Write the output to output_filename"""
    #     if self.output_filename is None:
    #         return
    #     assert self.output_filename is not None
    #     assert self.output is not None
    #     self.check_directory()
    #     logging.info(f"Writing output to {self.output_filename.name}")
    #     with open(self.output_filename, 'w', encoding="utf-8") as file:
    #         file.write(self.output)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.config_filename}')"
