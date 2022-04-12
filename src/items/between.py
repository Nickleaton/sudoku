from typing import List

from pulp import LpVariable, LpInteger

from src.glyphs.glyph import Glyph, BetweenGlyph
from src.items.board import Board
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule

EXCLUDE_VALUES_ON_LINE = False


class Between(Line):

    @property
    def name(self) -> str:
        if self.identity is None:
            cell_str = "".join([f"{cell.row}{cell.column}" for cell in self.cells])
            return f"{self.__class__.__name__}_{cell_str}"
        return f"{self.__class__.__name__}_{self.identity}"

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

    def add_variables(self, board: Board, solver: PulpSolver) -> None:
        self.identity = len(solver.betweens) + 1
        solver.betweens[self.name] = LpVariable(f"{self.name}_increasing", 0, 1, LpInteger)

    def add_constraint(self, solver: PulpSolver) -> None:
        # noinspection PyPep8Naming
        M = solver.board.maximum_digit + 1

        start_cell = self.cells[0]
        start = solver.values[start_cell.row][start_cell.column]

        end_cell = self.cells[-1]
        end = solver.values[end_cell.row][end_cell.column]

        for cell in self.cells[1:-1]:
            value = solver.values[cell.row][cell.column]
            flag = solver.betweens[self.name]

            # Ascending
            label = f"{self.name}_after_ascending_{cell.row}_{cell.column}"
            solver.model += start + 1 <= M * flag + value, label

            label = f"{self.name}_before_ascending_{cell.row}_{cell.column}"
            solver.model += value + 1 <= M * flag + end, label

            # Descending
            label = f"{self.name}_after_descending_{cell.row}_{cell.column}"
            solver.model += start + M * (1 - flag) >= value + 1, label

            label = f"{self.name}_before_descending_{cell.row}_{cell.column}"
            solver.model += value + M * (1 - flag) >= end + 1, label

        if EXCLUDE_VALUES_ON_LINE:
            # min and max digit cannot be in the middle of a between line
            for cell in self.cells[1:-1]:
                solver.model += solver.choices[self.board.minimum_digit][cell.row][cell.column] == 0
                solver.model += solver.choices[self.board.maximum_digit][cell.row][cell.column] == 0
