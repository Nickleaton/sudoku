from typing import List, Dict, Callable

from src.glyphs.glyph import Glyph
from src.glyphs.frozen_thermometer_glyph import FrozenThermometerGlyph
from src.items.box import Box
from src.items.column import Column
from src.items.item import Item
from src.items.row import Row
from src.items.thermometer import Thermometer
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class FrozenThermometer(Thermometer):

    @property
    def rules(self) -> List[Rule]:
        return [Rule('FrozenThermo', 1, "Cells along a line with a bulb increase or stay the same from the bulb end")]

    def glyphs(self) -> List[Glyph]:
        return [
            FrozenThermometerGlyph('FrozenThermometer', [cell.coord for cell in self.cells])
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Frozen Thermometer'})

    def add_constraint(self, solver: PulpSolver) -> None:
        for i in range(1, len(self)):
            cell_1 = self.cells[i - 1]
            cell_2 = self.cells[i]

            unique = {Box, Row, Column}
            region_1 = {region for region in cell_1.top.regions() if region.__class__ in unique}
            region_2 = {region for region in cell_2.top.regions() if region.__class__ in unique}

            name = f"{self.__class__.__name__}_rank_{cell_1.row}_{cell_1.column}_{cell_2.row}_{cell_2.column}"
            lower = solver.values[cell_1.row][cell_1.column]
            upper = solver.values[cell_2.row][cell_2.column]
            if len(region_1.intersection(region_2)) == 0:
                solver.model += lower <= upper, name
            else:
                solver.model += lower + 1 <= upper, name

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
