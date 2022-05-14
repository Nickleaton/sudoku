import logging
from typing import Dict

import oyaml as yaml

from src.items.board import Board
from src.items.item import Item
from src.items.solution import Solution


class Command:

    def __init__(self, config_filename: str, output_filename: str):
        self.config_filename: str = config_filename
        self.config: Dict = None
        self.board: Board = None
        self.problem: Item = None
        self.solution: Solution = None
        self.output_filename = output_filename
        self.output: str = None

    def load_config(self) -> None:
        logging.info(f"Loading config from {self.config_filename}")
        with open(self.config_filename, 'r') as f:
            self.config = yaml.load(f, yaml.SafeLoader)

    def create_board(self):
        logging.info(f"Creating board")
        self.board = Board.create('Board', self.config)

    def create_problem(self):
        logging.info(f"Creating problem")
        self.problem = Item.create(self.board, {'Constraints': self.config['Constraints']})

    def process(self) -> None:
        self.load_config()
        self.create_board()
        self.create_problem()

    def write(self) -> None:
        logging.info(f"Writing output to {self.output_filename}")
        with open(self.output_filename, 'w', encoding="utf-8") as f:
            f.write(self.output)
