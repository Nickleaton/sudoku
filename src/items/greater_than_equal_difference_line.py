import re
from typing import List, Sequence

from src.items.board import Board
from src.items.cell import Cell
from src.items.difference_line import DifferenceLine
from src.items.greater_than_equal_difference_pair import GreaterThanEqualDifferencePair
from src.solvers.formulations import Formulations
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class GreaterThanEqualDifferenceLine(DifferenceLine):

    def __init__(self, board: Board, cells: Sequence[Cell], difference: int = 0):
        super().__init__(board, cells, difference)
        for i in range(1, len(cells)):
            self.add(GreaterThanEqualDifferencePair(self.board, cells[i - 1], cells[i], self.difference))

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                self.__class__.__name__,
                1,
                f"Any two cells directly connected by a line must have a difference of at least {self.difference}"
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Difference', 'Comparison'})

    def add_constraint(self, solver: PulpSolver, include: re.Pattern, exclude: re.Pattern) -> None:
        for i in range(0, len(self.cells) - 1):
            x_1 = solver.values[self.cells[i].row][self.cells[i].column]
            x_2 = solver.values[self.cells[i + 1].row][self.cells[i + 1].column]
            name = f"{self.name}_{i}"
            solver.model += Formulations.abs(solver, x_1, x_2, self.board.maximum_digit) >= self.difference, name
