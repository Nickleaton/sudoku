from typing import List, Set, Dict

from pulp import LpVariable, LpInteger

from src.glyphs.glyph import Glyph, PolyLineGlyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Sequence(Line):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'Sequence',
                1,
                (
                    "Digits along grey lines follow arithmetic sequences."
                    "It means they go in increasing order from one end to the other, "
                    "and that the difference between all pairs of consecutive cells along the line is constant."
                )
            )
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [PolyLineGlyph('Sequence', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Sequence', 'Difference'})

    @staticmethod
    def max_diffence(length: int) -> int:
        if length == 1:
            return 9
        if length == 2:
            return 8
        if length == 3:
            return 3
        if length == 4:
            return 2
        if length == 5:
            return 2
        return 1

    def possible_digits(self) -> List[Set[int]]:
        length = len(self.cells)
        big_m = self.board.maximum_digit

        possible = []
        for i in range(1, length + 1):
            a = set(range(i, i + big_m - length + 1))
            d = {big_m - x + 1 for x in range(i, i + big_m - length + 1)}
            possible.append(a.union(d))
        return possible

    def add_constraint(self, solver: PulpSolver) -> None:
        # Given there is an ascending sequence the cells must be unique
        # This also enforces that the gaps cannot go +2 -2 as an example
        self.add_unique_constraint(solver, optional=True)

        # create a variable for the difference
        max_diff = Sequence.max_diffence(len(self.cells))
        difference = LpVariable(self.name, -max_diff, max_diff, LpInteger)

        # for each pair set enforce that the delta is the difference
        for i in range(0, len(self.cells) - 1):
            value1 = solver.values[self.cells[i].row][self.cells[i].column]
            value2 = solver.values[self.cells[i + 1].row][self.cells[i + 1].column]
            solver.model += value1 - value2 == difference, f"{self.name}_{i}"

        # speeds up the solve by restricting the possible digits along the line
        # works like a double ended thermometer
        for i, possible in enumerate(self.possible_digits()):
            for d in self.board.digit_range:
                if d not in possible:
                    cell = self.cells[i]
                    name = f"{self.name}_impossible_{i}_{d}"
                    solver.model += solver.choices[d][cell.row][cell.column] == 0, name

    def css(self) -> Dict:
        return {
            ".Renban": {
                "stroke": "grey",
                "stroke-width": 20,
                "stroke-linecap": "round",
                "stroke-linejoin": "round",
                "fill-opacity": 0
            }
        }
