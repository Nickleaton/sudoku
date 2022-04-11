from itertools import product

from pulp import LpVariable, LpInteger, LpProblem, LpMinimize, LpStatus, LpStatusOptimal, lpSum

from src.items.board import Board
from src.items.solution import Solution
from src.solvers.solver import Solver


class PulpSolver(Solver):

    def __init__(self, board: Board):
        super().__init__(board)
        self.objective = 0, "Objective"
        self.model = LpProblem("Sudoku", LpMinimize)
        self.model += self.objective
        self.status = 'Pending'
        self.solution = None
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
        self.renbans = {}
        self.distinct_renbans = []
        self.betweens = {}

        for row, column in product(board.row_range, board.column_range):
            self.model += lpSum(digit * self.choices[digit][row][column] for digit in self.board.digit_range) == \
                          self.values[row][column], f"Unique_cell_{row}_{column}"

    def save(self, filename: str) -> None:
        self.model.writeLP(filename)

    def solve(self):
        self.model.solve()
        self.status = LpStatus[self.model.status]
        if self.model.status != LpStatusOptimal:
            return
        self.solution = Solution(self.board)
        for row in self.board.row_range:
            for column in self.board.column_range:
                self.solution.set_value(row, column, self.values[row][column].varValue)
