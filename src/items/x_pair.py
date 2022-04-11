from typing import List

from src.items.board import Board
from src.items.cell import Cell
from src.items.difference_pair import DifferencePair
from src.utils.rule import Rule


class XPair(DifferencePair):

    def __init__(self, board: Board, c1: Cell, c2: Cell):
        super().__init__(board, c1, c2)

    @property
    def difference(self):
        return 10

    @property
    def rules(self) -> List[Rule]:
        return [Rule("XPair", 1, "Cells separated by an X must have a difference of 10")]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'X'})
