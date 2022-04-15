from typing import List

from src.items.board import Board
from src.items.cell import Cell
from src.items.line import Line


class DifferenceLine(Line):

    def __init__(self, board: Board, cells: List[Cell], difference: int):
        super().__init__(board, cells)
        self.difference = difference

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Difference', 'Comparison'})
