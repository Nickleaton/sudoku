from typing import List

from src.glyphs.glyph import Glyph, SimpleThermometerGlyph
from src.items.thermometer import Thermometer
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class SimpleThermometer(Thermometer):

    @property
    def rules(self) -> List[Rule]:
        return [Rule('SimpleThermometer', 1, "Cells along a line with a bulb strictly increase from the bulb end")]

    @property
    def glyphs(self) -> List[Glyph]:
        return [
            SimpleThermometerGlyph('SimpleThermometer', [cell.coord for cell in self.cells])
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Simple Thermometer'})

    def add_constraint(self, solver: PulpSolver) -> None:
        for i in range(1, len(self)):
            c1 = self.cells[i - 1]
            c2 = self.cells[i]

            c1_value = solver.values[c1.row][c1.column]
            c2_value = solver.values[c2.row][c2.column]
            name = f"{self.__class__.__name__}_rank_{c1.row}_{c1.column}_{c2.row}_{c2.column}"
            solver.model += c1_value + 1 <= c2_value, name

            name = f"{self.__class__.__name__}_lbound_{c2.row}_{c2.column}"
            solver.model += c2_value >= i + 1, name

            name = f"{self.__class__.__name__}_ubound_{c2.row}_{c2.column}"
            solver.model += c2_value <= self.board.maximum_digit - len(self) + i + 1, name

        c2 = self.cells[0]
        c2_value = solver.values[c2.row][c2.column]
        name = f"{self.__class__.__name__}_lbound_{c2.row}_{c2.column}"
        solver.model += c2_value >= 0 + 1, name

        name = f"{self.__class__.__name__}_ubound_{c2.row}_{c2.column}"
        solver.model += c2_value <= self.board.maximum_digit - len(self) + 0 + 1, name
