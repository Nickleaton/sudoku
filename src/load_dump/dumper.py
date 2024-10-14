from abc import ABC, abstractmethod

from src.items.board import Board


class Dumper(ABC):

    def __init__(self, board: Board):
        self.board = board

    @abstractmethod
    def text(self) -> str:
        raise NotImplementedError
