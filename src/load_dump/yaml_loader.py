import oyaml as yaml

from src.items.board import Board
from src.load_dump.loader import Loader


class YamlLoader(Loader):

    def __init__(self, filename: str) -> None:
        super().__init__(filename)
        with open(self.filename) as file:
            self.raw = yaml.safe_load(file)

    def process(self) -> Board:
        return Board.create('Board', self.raw)
