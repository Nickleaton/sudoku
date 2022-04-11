from typing import List

from src.items.board import Board
from src.items.cell import Cell
from src.items.difference_pair import DifferencePair
from src.utils.rule import Rule


class VIPair(DifferencePair):

    def __init__(self, board: Board, c1: Cell, c2: Cell):
        super().__init__(board, c1, c2)

    @property
    def difference(self):
        return 6

    @property
    def rules(self) -> List[Rule]:
        return [Rule("VIPair", 1, "Cells separated by a VI must have a difference of 6")]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'VI'})
