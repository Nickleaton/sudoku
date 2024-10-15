from typing import List, Dict, Callable

from src.glyphs.glyph import Glyph
from src.glyphs.arrow_line_glyph import ArrowLineGlyph
from src.items.item import Item
from src.items.line import Line
from src.solvers.formulations import Formulations
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class MaxArrow(Line):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'MaxArrow',
                1,
                "The digit in the bulb is the maximum of the digits on the arrow"
            )
        ]

    def glyphs(self) -> List[Glyph]:
        return [ArrowLineGlyph('Arrow', [cell.coord for cell in self.cells])]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Arrow', 'Maximum'})

    def css(self) -> Dict:
        return {
            '.Arrow': {
                'stroke': 'grey',
                'fill': 'white',
                'stroke-width': 3
            },
            '.MaxArrowStart': {
            },
            '.MaxArrowEnd': {
                'fill-opacity': 0
            }
        }

    def add_constraint(self, solver: PulpSolver) -> None:
        bulb = solver.values[self.cells[0].row][self.cells[0].column]
        values = [solver.values[self.cells[i].row][self.cells[i].column] for i in range(1, len(self.cells))]
        value = Formulations.maximum(solver.model, values, 1, self.board.maximum_digit)
        solver.model += bulb == value, self.name
