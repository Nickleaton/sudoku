from abc import ABC
from pathlib import Path

from src.items.board import Board


class LoaderError(Exception):
    pass


class Loader(ABC):

    def __init__(self, filename: str) -> None:
        self.filename = Path(filename)

    def process(self) -> Board:
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} ({repr(self.filename)})"
