import re
from typing import List, Dict

from pulp import LpVariable, LpInteger

from src.glyphs.glyph import Glyph, BetweenGlyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule

EXCLUDE_VALUES_ON_LINE = False


class Between(Line):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'Between',
                1,
                "Cells along lines between two filled circles must have values strictly between those in the circles"
            )
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [BetweenGlyph('Between', [cell.coord for cell in self.cells])]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Between', 'Comparison'})

    def add_constraint(self, solver: PulpSolver, include: re.Pattern, exclude: re.Pattern) -> None:
        big_m = solver.board.maximum_digit + 1

        start_cell = self.cells[0]
        start = solver.values[start_cell.row][start_cell.column]

        end_cell = self.cells[-1]
        end = solver.values[end_cell.row][end_cell.column]

        flag = LpVariable(f"{self.name}_increasing", 0, 1, LpInteger)

        for cell in self.cells[1:-1]:
            value = solver.values[cell.row][cell.column]

            # Ascending
            label = f"{self.name}_after_ascending_{cell.row}_{cell.column}"
            solver.model += start + 1 <= big_m * flag + value, label

            label = f"{self.name}_before_ascending_{cell.row}_{cell.column}"
            solver.model += value + 1 <= big_m * flag + end, label

            # Descending
            label = f"{self.name}_after_descending_{cell.row}_{cell.column}"
            solver.model += start + big_m * (1 - flag) >= value + 1, label

            label = f"{self.name}_before_descending_{cell.row}_{cell.column}"
            solver.model += value + big_m * (1 - flag) >= end + 1, label

            solver.model += solver.choices[1][cell.row][cell.column] == 0, \
                            f"{self.name}_s_{1}_{cell.row}_{cell.column}"
            solver.model += solver.choices[self.board.maximum_digit][cell.row][cell.column] == 0, \
                            f"{self.name}_e_{1}_{cell.row}_{cell.column}"
    def css(self) -> Dict:
        return {
            '.Between': {
                'stroke': 'grey',
                'fill': 'white',
                'stroke-width': 3
            },
            '.BetweenStart': {
            },
            '.BetweenEnd': {
            }
        }
