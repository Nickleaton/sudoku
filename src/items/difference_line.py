from typing import Sequence

from src.items.board import Board
from src.items.cell import Cell
from src.items.line import Line


class DifferenceLine(Line):

    def __init__(self, board: Board, cells: Sequence[Cell], difference: int):
        super().__init__(board, cells)
        self.difference = difference

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Difference', 'Comparison'})
