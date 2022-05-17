import logging
import os.path
from typing import Dict, Optional

import oyaml as yaml

from src.items.board import Board
from src.items.item import Item
from src.items.solution import Solution


class Command:

    def __init__(self, config_filename: str, output_filename: Optional[str] = None):
        self.config_filename: str = config_filename
        self.config: Optional[Dict] = None
        self.board: Optional[Board] = None
        self.problem: Optional[Item] = None
        self.solution: Optional[Solution] = None
        self.output_filename: Optional[str] = output_filename
        self.output: Optional[str] = None

    def load_config(self) -> None:
        logging.info(f"Loading config from {self.config_filename}")
        with open(self.config_filename, 'r', encoding='utf-8') as file:
            self.config = yaml.load(file, yaml.SafeLoader)

    def create_board(self):
        logging.info("Creating board")
        self.board = Board.create('Board', self.config)

    def create_problem(self):
        logging.info("Creating problem")
        self.problem = Item.create(self.board, {'Constraints': self.config['Constraints']})

    def process(self) -> None:
        self.load_config()
        self.create_board()
        self.create_problem()
        self.output = ""

    def check_directory(self) -> None:
        assert self.output_filename is not None
        directory: str = os.path.dirname(self.output_filename)
        if not os.path.exists(directory):  # pragma: no cover
            logging.info(f"Creating directory {directory}")
            os.makedirs(directory)

    def write(self) -> None:
        if self.output_filename is None:
            return
        assert self.output_filename is not None
        assert self.output is not None
        self.check_directory()
        logging.info(f"Writing output to {self.output_filename}")
        with open(self.output_filename, 'w', encoding="utf-8") as file:
            file.write(self.output)
