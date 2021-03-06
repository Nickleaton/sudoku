from typing import Sequence, List

from src.items.board import Board
from src.items.cell import Cell
from src.items.line import Line


class DifferenceLine(Line):

    def __init__(self, board: Board, cells: Sequence[Cell], difference: int = 0):
        super().__init__(board, cells)
        self.difference = difference
        self.excluded: List[int] = []

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Difference', 'Comparison'})

    # def add_constraint(self, solver: PulpSolver) -> None:
    #     # Other rules handled in the pair
    #     # exclude excluded
    #     for cell, digit in product(self.cells, self.excluded):
    #         name = f"Excluded_{cell.name}_{digit}"
    #         solver.model += solver.choices[digit][cell.row][cell.column] == 0, name
