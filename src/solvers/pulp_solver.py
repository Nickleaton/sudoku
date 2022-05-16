from itertools import product
from typing import Optional

from pulp import LpVariable, LpInteger, LpProblem, LpMinimize, LpStatus, LpStatusOptimal, lpSum, getSolver

from src.items.board import Board
from src.items.solution import Solution
from src.solvers.solver import Solver


class PulpSolver(Solver):  # pylint: disable=too-many-instance-attributes

    def __init__(self, board: Board, solver_name: str = 'PULP_CBC_CMD'):
        super().__init__(board)
        self.solver_name = solver_name
        self.application = getSolver(solver_name)

        self.objective = 0, "Objective"
        self.model = LpProblem("Sudoku", LpMinimize)
        self.model += self.objective
        self.status = 'Pending'
        self.solution: Optional[Solution] = None
        self.choices = LpVariable.dicts("Choice",
                                        (board.digit_range, board.row_range, board.column_range),
                                        0,
                                        1,
                                        LpInteger
                                        )
        self.values = LpVariable.dicts("Values",
                                       (board.row_range, board.column_range),
                                       1,
                                       board.maximum_digit,
                                       LpInteger
                                       )

        for row, column in product(board.row_range, board.column_range):
            total = lpSum(digit * self.choices[digit][row][column] for digit in self.board.digit_range)
            self.model += total == self.values[row][column], f"Unique_cell_{row}_{column}"

    def save(self, filename: str) -> None:
        super().save(filename)
        self.model.writeLP(filename)

    def solve(self) -> None:
        super().solve()
        self.model.solve(self.application)
        self.status = LpStatus[self.model.status]
        if self.model.status != LpStatusOptimal:
            return
        self.solution = Solution(self.board)
        for row in self.board.row_range:
            for column in self.board.column_range:
                self.solution.set_value(row, column, int(self.values[row][column].varValue))
