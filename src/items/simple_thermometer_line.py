"""SimpleThermometerLine."""

from src.glyphs.glyph import Glyph
from src.glyphs.simple_thermometer_glyph import SimpleThermometerGlyph
from src.items.thermometer_line import ThermometerLine
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class SimpleThermometerLine(ThermometerLine):
    """Simple thermometer line.

    Cells along the line must strictly increase from the bulb end.
    """

    @property
    def rules(self) -> list[Rule]:
        """Get the rules associated with the Simple Thermometer line.

        Returns:
            list[Rule]: A list of rules specific to the Simple Thermometer line.
        """
        return [Rule('SimpleThermometerLine', 1,
                     "Cells along start line with start bulb strictly increase from the bulb end")]

    def glyphs(self) -> list[Glyph]:
        """Generate glyph representations for the Simple Thermometer line.

        Returns:
            list[Glyph]: A list of glyphs representing the Simple Thermometer line.
        """
        return [
            SimpleThermometerGlyph('SimpleThermometerLine', [cell.coord for cell in self.cells])
        ]

    @property
    def tags(self) -> set[str]:
        """Tags associated with the Simple Thermometer line.

        Returns:
            set[str]: A set of tags specific to the Simple Thermometer line.
        """
        return super().tags.union({'SimpleThermometerLine'})

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints.

        Args:
            solver (PulpSolver): The solver instance to which the constraints are added.
        """
        for i in range(1, len(self.cells)):
            c1 = self.cells[i - 1]
            c2 = self.cells[i]

            c1_value = solver.values[c1.row][c1.column]
            c2_value = solver.values[c2.row][c2.column]

            # C1 < C2
            name = f"{self.name}_rank_{c1.row}_{c1.column}_{c2.row}_{c2.column}"
            solver.model += c1_value + 1 <= c2_value, name

        for i, cell in enumerate(self.cells):
            # Bounds
            lower: int = i + 1
            upper: int = self.board.maximum_digit - len(self) + i + 1

            # pylint: disable=unnecessary-comprehension
            possible: set[int] = {i for i in range(lower, upper + 1)}
            for digit in self.board.digit_range:
                if digit not in possible:
                    solver.model += solver.choices[digit][cell.row][cell.column], f"{self.name}_{cell.name}_{digit}"
