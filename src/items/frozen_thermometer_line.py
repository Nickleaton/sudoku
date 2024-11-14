from typing import List, Dict

from src.glyphs.frozen_thermometer_glyph import FrozenThermometerGlyph
from src.glyphs.glyph import Glyph
from src.items.box import Box
from src.items.column import Column
from src.items.row import Row
from src.items.thermometer_line import ThermometerLine
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class FrozenThermometerLine(ThermometerLine):
    """Represents a frozen thermometer line.

    The cells along the line must increase or stay the same from the bulb end.
    """

    @property
    def rules(self) -> List[Rule]:
        """Get the rules associated with the Frozen Thermometer line.

        Returns:
            List[Rule]: A list of rules specific to the Frozen Thermometer line.
        """
        return [Rule('FrozenThermometerLine', 1,
                     "Cells along a line with a bulb increase or stay the same from the bulb end")]

    def glyphs(self) -> List[Glyph]:
        """Generate glyph representations for the Frozen Thermometer line.

        Returns:
            List[Glyph]: A list of glyphs representing the Frozen Thermometer line.
        """
        return [
            FrozenThermometerGlyph('FrozenThermometerLine', [cell.coord for cell in self.cells])
        ]

    @property
    def tags(self) -> set[str]:
        """Tags associated with the Frozen Thermometer line.

        Returns:
            set[str]: A set of tags specific to the Frozen Thermometer line.
        """
        return super().tags.union({'Frozen', 'FrozenThermometerLine'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the solver for the Frozen Thermometer line.

        Args:
            solver (PulpSolver): The solver instance to which the constraints are added.
        """
        for i in range(1, len(self.cells)):
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
        """Define CSS styling properties for rendering the Frozen Thermometer line.

        Returns:
            Dict: A dictionary defining CSS properties for the Frozen Thermometer line.
        """
        return {
            '.FrozenThermometerLine': {
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
