import re
from typing import List, Optional

from src.items.board import Board
from src.items.cell import Cell
from src.items.standard_region import StandardRegion
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Row(StandardRegion):

    def __init__(self, board: Board, index: int):
        super().__init__(board, index)
        self.add_items([Cell.make(board, index, row) for row in board.row_range])
        self.strict = True
        self.unique = True

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Row', 1, 'Digits in each row must be unique')]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Row'})

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_total_constraint(solver, solver.board.digit_sum)
        self.add_unique_constraint(solver)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.index})"
