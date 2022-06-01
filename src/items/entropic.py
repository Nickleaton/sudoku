import re
from typing import List, Dict, Optional

from pulp import LpAffineExpression, lpSum

from src.glyphs.glyph import Glyph, PolyLineGlyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Entropic(Line):

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
        # enforce that you cannot have a low next to a low, mid next to a mid, and top next to a top
        for i in range(0, len(self.cells) - 1):
            pname = f"{self.cells[i].row}_{self.cells[i].column}_{self.cells[i + 1].row}_{self.cells[i + 1].column}"
            solver.model += self.low_total(solver, i) + self.low_total(solver, i + 1) <= 1, f"{self.name}_a_low_{pname}"
            solver.model += self.mid_total(solver, i) + self.mid_total(solver, i + 1) <= 1, f"{self.name}_a_mid_{pname}"
            solver.model += self.top_total(solver, i) + self.top_total(solver, i + 1) <= 1, f"{self.name}_a_top_{pname}"
        # enforce that every 3 cells along a line we get the same 'entropicness'
        for i in range(0, len(self.cells) - 3):
            pname = f"{self.cells[i].row}_{self.cells[i].column}_{self.cells[i + 3].row}_{self.cells[i + 3].column}"
            solver.model += self.low_total(solver, i) == self.low_total(solver, i + 3), f"{self.name}_j_low_{pname}"
            solver.model += self.mid_total(solver, i) == self.mid_total(solver, i + 3), f"{self.name}_j_mid_{pname}"
            solver.model += self.top_total(solver, i) == self.top_total(solver, i + 3), f"{self.name}_j_top_{pname}"

    def css(self) -> Dict:
        return {
            '.Entropic': {
                'stroke': 'orange',
                'stroke-width': 10,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0
            }
        }
