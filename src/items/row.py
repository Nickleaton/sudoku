from typing import List

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.standard_region import StandardRegion
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Row(StandardRegion):

    def __init__(self, board: Board, index: int):
        super().__init__(board, index)
        self.add_items([Cell.make(board, index, row) for row in board.row_range])

    @property
    def glyphs(self) -> List[Glyph]:
        result = []
        for item in self.items:
            result.extend(item.glyphs)
        return result

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Row', 1, 'Digits in each row must be unique')]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Row'})

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_total_constraint(solver, solver.board.digit_sum, self.name)
        self.add_unique_constraint(solver, f"Row_{self.index!r}")
