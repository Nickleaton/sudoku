import re
from typing import List, Dict

from pulp import lpSum

from src.glyphs.glyph import Glyph, ArrowLineGlyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Arrow(Line):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'Arrow',
                1,
                "Digits along an arrow must sum to the digit in its circle. Digits may repeat along an arrow"
            )
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [ArrowLineGlyph('Arrow', [cell.coord for cell in self.cells])]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Arrow', 'Sum'})

    def add_constraint(self, solver: PulpSolver, include: re.Pattern, exclude: re.Pattern) -> None:
        total = lpSum([solver.values[self.cells[i].row][self.cells[i].column] for i in range(1, len(self))])
        solver.model += total == solver.values[self.cells[0].row][self.cells[0].column], self.name

    def css(self) -> Dict:
        return {
            '.Arrow': {
                'stroke': 'grey',
                'fill': 'white',
                'stroke-width': 3
            },
            '.ArrowStart': {
            },
            '.ArrowEnd': {
                'fill-opacity': 0
            }
        }
