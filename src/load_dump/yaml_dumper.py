from src.items.board import Board
from src.load_dump.dumper import Dumper


class YamlDumper(Dumper):

    def __init__(self, board: Board):
        super().__init__(board)

