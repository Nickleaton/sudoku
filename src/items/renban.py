from typing import List

from pulp import LpVariable, LpInteger

from src.glyphs.glyph import Glyph, PolyLineGlyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Renban(Line):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'Renban',
                1,
                "Pink lines must contain a set of consecutive, non-repeating digits, in any order"
            )
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [PolyLineGlyph('Renban', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Renban', 'Adjacent', 'Set'})

    def add_constraint(self, solver: PulpSolver) -> None:
        # unique on lines
        self.add_unique_constraint(solver)

        # lower and upper bounds for the line.
        # Upper is greater than or equal to all values on the line
        # Lower is less than or equal to all values on the line
        # The difference of the lower and the upper is the length of the line less one.

        # eg. 4 6 5 on the line. We have to force upper - lower = 3 - 1
        # 6 - 4 = 2 = length - 1 = 3 - 1 = 2

        lower = LpVariable(f"{self.name}_lower", 1, self.board.maximum_digit, LpInteger)
        upper = LpVariable(f"{self.name}_upper", 1, self.board.maximum_digit, LpInteger)

        # handle upper and lower
        for cell in self.cells:
            value = solver.values[cell.row][cell.column]
            solver.model += lower <= value, f"{self.name}_lower_{cell.row}_{cell.column}"
            solver.model += upper >= value, f"{self.name}_upper_{cell.row}_{cell.column}"

        # set the difference constraint
        solver.model += upper - lower == len(self.cells) - 1, f"{self.name}_range_{len(self.cells) - 1}"
