from typing import List, Dict, Callable

from pulp import lpSum

from src.glyphs.glyph import Glyph
from src.glyphs.arrow_line_glyph import ArrowLineGlyph
from src.items.item import Item
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class ProductArrow(Line):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'Arrow',
                1,
                "Digits along an arrow, when multiplied together will give the digit in its circle. "
                "Digits may repeat along an arrow if allowed by other rules"
            )
        ]

    def glyphs(self, selector: Callable[[Item], bool]) -> List[Glyph]:
        return [ArrowLineGlyph('Arrow', [cell.coord for cell in self.cells])]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Arrow', 'Product'})

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

    def add_constraint(self, solver: PulpSolver) -> None:
        # TODO
        pass
