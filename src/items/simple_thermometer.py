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

            # C1 < C2
            name = f"{self.name}_rank_{c1.row}_{c1.column}_{c2.row}_{c2.column}"
            solver.model += c1_value + 1 <= c2_value, name

        for i, cell in enumerate(self.cells):
            # Bounds
            lower = i + 1
            upper = self.board.maximum_digit - len(self) + i + 1
            possible = set(range[lower, upper + 1])
            for digit in self.board.digit_range:
                if digit not in possible:
                    solver.model += solver.choices[digit][cell.row][cell.column], f"{self.name}_{cell.name}_{digit}"

                    # c2 = self.cells[0]
        # c2_value = solver.values[c2.row][c2.column]
        # name = f"{self.name}_lbound_{c2.row}_{c2.column}"
        # solver.model += c2_value >= 0 + 1, name
        #
        # name = f"{self.name}_ubound_{c2.row}_{c2.column}"
        # solver.model += c2_value <= self.board.maximum_digit - len(self) + 0 + 1, name
