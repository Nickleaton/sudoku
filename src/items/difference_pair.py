from typing import List, Dict

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
    def create(cls, name: str, board: Board, yaml: Dict) -> Item:
        c1 = Cell(board, yaml['Cells'][0][0], yaml['Cells'][0][1])
        c2 = Cell(board, yaml['Cells'][1][0], yaml['Cells'][1][1])
        difference = yaml['Difference']
        return cls(board, c1, c2, difference)

    @property
    def rules(self) -> List[Rule]:
        return []

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Difference'})

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.c1!r}, {self.c2!r}, {self.difference!r})"
