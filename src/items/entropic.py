from typing import Optional, List

from pulp import LpAffineExpression, lpSum

from src.glyphs.glyph import Glyph, PolyLineGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Entropic(Line):

    def __init__(self, board: Board, cells: Optional[List[Cell]]):
        super().__init__(board, cells)

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'Entropic',
                1,
                (
                    "Any sequence of 3 successive digits along a golden line must include "
                    "a low (123), a medium (456) and a high (789) digit"
                )
            )
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [PolyLineGlyph('Entropic', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Entropic', 'Set'})

    def low_total(self, solver: PulpSolver, n: int) -> LpAffineExpression:
        return lpSum([solver.choices[digit][self.cells[n].row][self.cells[n].column] for digit in [1, 2, 3]])

    def mid_total(self, solver: PulpSolver, n: int) -> LpAffineExpression:
        return lpSum([solver.choices[digit][self.cells[n].row][self.cells[n].column] for digit in [4, 5, 6]])

    def top_total(self, solver: PulpSolver, n: int) -> LpAffineExpression:
        return lpSum([solver.choices[digit][self.cells[n].row][self.cells[n].column] for digit in [7, 8, 9]])

    def add_constraint(self, solver: PulpSolver) -> None:
        for n in range(1, len(self.cells) - 3):
            pname = f"{self.cells[n].row}_{self.cells[n].column}_{self.cells[n + 3].row}_{self.cells[n + 3].column}"
            solver.model += self.low_total(solver, n) == self.low_total(solver, n + 3), f"{self.name}_low_{pname}"
            solver.model += self.mid_total(solver, n) == self.mid_total(solver, n + 3), f"{self.name}_mid_{pname}"
            solver.model += self.top_total(solver, n) == self.top_total(solver, n + 3), f"{self.name}_top_{pname}"
