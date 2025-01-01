"""FrozenThermometerLine."""
from src.glyphs.glyph import Glyph
from src.glyphs.thermometer_glyph import ThermometerGlyph
from src.items.box import Box
from src.items.column import Column
from src.items.row import Row
from src.items.thermometer_line import ThermometerLine
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class FrozenThermometerLine(ThermometerLine):
    """Represents start frozen thermometer line.

    The cells along the line must increase or stay the same from the bulb end.
    """

    @property
    def rules(self) -> list[Rule]:
        """Get the rules associated with the Frozen Thermometer line.

        Returns:
            list[Rule]: A list of rules specific to the Frozen Thermometer line.
        """
        rule_text: str = 'Cells along start line with start bulb increase or stay the same from the bulb end'
        return [Rule(self.__class__.__name__, 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Generate glyph representations for the Frozen Thermometer line.

        Returns:
            list[Glyph]: A list of glyphs representing the Frozen Thermometer line.
        """
        return [ThermometerGlyph(self.__class__.__name__, [cell.coord for cell in self.cells])]

    @property
    def tags(self) -> set[str]:
        """Tags associated with the Frozen Thermometer line.

        Returns:
            set[str]: A set of tags specific to the Frozen Thermometer line.
        """
        return super().tags.union({'Frozen', self.__class__.__name__})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the solver for the Frozen Thermometer line.

        Args:
            solver (PulpSolver): The solver instance to which the constraints are added.
        """
        for cell1, cell2 in zip(self.cells[:-1], self.cells[1:]):
            unique = {Box, Row, Column}
            region1 = {region for region in cell1.top.regions() if region.__class__ in unique}
            region2 = {region for region in cell2.top.regions() if region.__class__ in unique}

            name = f'{self.__class__.__name__}_rank_{cell1.row}_{cell1.column}_{cell2.row}_{cell2.column}'
            lower = solver.cell_values[cell1.row][cell1.column]
            upper = solver.cell_values[cell2.row][cell2.column]
            if region1.intersection(region2):
                solver.model += lower <= upper, name
            else:
                solver.model += lower + 1 <= upper, name

    def css(self) -> dict:
        """Define CSS styling properties for rendering the Frozen Thermometer line.

        Returns:
            dict: A dictionary defining CSS properties for the Frozen Thermometer line.
        """
        return {
            '.FrozenThermometerLine': {
                'stroke': 'grey',
                'stroke-width': 20,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0,
            },
            '.FrozenThermometerStart': {
                'stroke': 'grey',
                'fill': 'grey',
                'stroke-width': 30,
            },
        }
