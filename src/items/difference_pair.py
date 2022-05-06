from typing import List, Any, Tuple

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.pair import Pair
from src.utils.rule import Rule


class DifferencePair(Pair):

    def __init__(self, board: Board, c1: Cell, c2: Cell, difference: int):
        super().__init__(board, c1, c2)
        self.difference = difference

    @classmethod
    def extract(cls, board: Board, yaml: Any) -> Tuple:
        cs, ds = yaml[cls.__name__].split('=')
        c1s, c2s = cs.split("-")
        c1 = Cell.make(board, int(c1s[0]), int(c1s[1]))
        c2 = Cell.make(board, int(c2s[0]), int(c2s[1]))
        return c1, c2, int(ds)

    @classmethod
    def create(cls, board: Board, yaml: Any) -> Item:
        c1, c2, difference = cls.extract(board, yaml)
        return cls(board, c1, c2, difference)

    @property
    def rules(self) -> List[Rule]:
        return []

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Difference'})

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.c1!r}, {self.c2!r}, {self.difference!r})"
