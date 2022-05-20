import re
from typing import List, Dict

from src.glyphs.glyph import Glyph, FrozenThermometerGlyph
from src.items.thermometer import Thermometer
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class FrozenThermometer(Thermometer):

    @property
    def rules(self) -> List[Rule]:
        return [Rule('FrozenThermo', 1, "Cells along a line with a bulb increase or stay the same from the bulb end")]

    @property
    def glyphs(self) -> List[Glyph]:
        return [
            FrozenThermometerGlyph('FrozenThermometer', [cell.coord for cell in self.cells])
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Frozen Thermometer'})

    def add_constraint(self, solver: PulpSolver, include: re.Pattern, exclude: re.Pattern) -> None:
        for i in range(1, len(self)):
            c1 = self.cells[i - 1]
            c2 = self.cells[i]

            name = f"{self.__class__.__name__}_rank_{c1.row}_{c1.column}_{c2.row}_{c2.column}"
            solver.model += solver.values[c1.row][c1.column] <= solver.values[c2.row][c2.column], name

    def css(self) -> Dict:
        return {
            '.FrozenThermometer': {
                'stroke': 'grey',
                'stroke-width': 20,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0
            },
            '.FrozenThermometerStart': {
                'stroke': 'grey',
                'fill': 'grey',
                'stroke-width': 30
            }
        }
