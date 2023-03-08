from abc import ABC

from src.items.board import Board


class Dumper(ABC):

    def __init__(self, board: Board):
        self.board = board

    def text(self) -> str:
        pass
