from typing import List, Set

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

    def mandatory_digits(self, length: int) -> Set[int]:
        """
        For a Renban line we can in some cases determine some of the digits on the line.

        So for a 1-9 digit set, if the line is 5 cells long, then we could have 1,2,3,4,5 which has a 5 on it.
        The same for all the other lines up to the line 5,6,7,8,9. So there is always a 5 on a 5 cell
        renban line of 9 possible dights.

        For a 6 cell line, we could have 1,2,3,4,5,6 as the lowest, and the highest is 4,5,6,7,8,9. The intersection
        is 4,5,6

        :param length:
        :return:
        """
        left = set(range(1, length + 1))
        right = set(range(self.board.maximum_digit, self.board.maximum_digit - length, -1))
        return left & right

    def add_constraint(self, solver: PulpSolver) -> None:
        # unique on lines
        self.add_unique_constraint(solver, True)

        # lower and upper bounds for the line.
        # Upper is greater than or equal to all values on the line
        # Lower is less than or equal to all values on the line
        # The difference of the lower and the upper is the length of the line less one.

        # eg. 4 6 5 on the line. We have to force upper - lower = 3 - 1
        # 6 - 4 = 2 = length - 1 = 3 - 1 = 2

        lower = LpVariable(f"{self.name}_lower", 1, self.board.maximum_digit, LpInteger)
        upper = LpVariable(f"{self.name}_upper", 1, self.board.maximum_digit, LpInteger)

        # Use a set of cells so the Renbans can be closed loops
        cells = set(self.cells)
        length = len(cells)

        # handle upper and lower
        for i, cell in enumerate(cells):
            value = solver.values[cell.row][cell.column]
            solver.model += lower <= value, f"{self.name}_lower_{i}"
            solver.model += upper >= value, f"{self.name}_upper_{i}"

        # set the difference constraint
        solver.model += upper - lower == length - 1, f"{self.name}_range_{length - 1}"

        # add the mandatory digits
        self.add_contains_constraint(solver, self.mandatory_digits(length))

    def css(self) -> str:
        return (
            ".Renban {\n"
            "    stroke: purple;\n"
            "    stroke-width: 20;\n"
            "    stroke-linecap: round;\n"
            "    stroke-linejoin: round;\n"
            "    fill-opacity: 0\n"
            "}\n"
        )

    def css2(self):
        return {
            ".Renban": {
                "stroke": "purple",
                "stroke-width": 20,
                "stroke-linecap": "round",
                "stroke-linejoin": "round",
                "fill-opacity": 0
            }
        }
