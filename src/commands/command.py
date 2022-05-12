import os.path

import oyaml as yaml

from src.items.board import Board
from src.items.item import Item


class Command:

    def __init__(self, filename: str):
        self.filename = filename
        self.config = None
        self.board = None
        self.problem = None
        self.solution = None
        self.output = None

    @property
    def extension(self) -> str:
        return ""

    def load_config(self) -> None:
        with open(self.filename, 'r') as f:
            self.config = yaml.load(f, yaml.SafeLoader)

    def create_board(self):
        self.board = Board.create('Board', self.config)

    def create_problem(self):
        self.problem = Item.create(self.board, {'Constraints': self.config['Constraints']})

    def process(self) -> None:
        pass

    def write(self, filename) -> None:
        rootname = os.path.basename(filename).split('.')[0]
        dirname = os.path.dirname(filename)
        filename = os.path.join(dirname, rootname + "." + self.extension)
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(self.output)
