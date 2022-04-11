from typing import List

from src.items.board import Board
from src.items.cell import Cell
from src.items.difference_pair import DifferencePair
from src.utils.rule import Rule


class ConsecutivePair(DifferencePair):

    def __init__(self, board: Board, c1: Cell, c2: Cell):
        super().__init__(board, c1, c2)

    @property
    def difference(self):
        return 1

    @property
    def rules(self) -> List[Rule]:
        return [Rule("ConsecutivePair", 1, "Cells separated by a white dot must be consecutive")]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Consecutive'})
