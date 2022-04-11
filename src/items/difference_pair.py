from typing import List

from src.items.board import Board
from src.items.cell import Cell
from src.items.pair import Pair
from src.utils.rule import Rule


class DifferencePair(Pair):

    def __init__(self, board: Board, c1: Cell, c2: Cell):
        super().__init__(board, c1, c2)

    @property
    def difference(self) -> int:
        return 0

    @property
    def rules(self) -> List[Rule]:
        return []

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Difference'})