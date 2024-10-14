from itertools import product
from pathlib import Path
from typing import Optional, Dict

import orloge
from pulp import LpVariable, LpInteger, LpProblem, LpMinimize, LpStatus, LpStatusOptimal, lpSum, getSolver

from src.items.board import Board
from src.solvers.answer import Answer
from src.solvers.solver import Solver


class PulpSolver(Solver):  # pylint: disable=too-many-instance-attributes

    def __init__(self, board: Board, name: str, log_file: Path, solver_name: str = 'PULP_CBC_CMD'):
        super().__init__(board)
        self.name = name
        self.log_file = log_file
        self.solver_name = solver_name
        if solver_name == 'PULP_CBC_CMD':
            self.application_name = 'CBC'
        self.log_file.unlink(missing_ok=True)
        self.application = getSolver(solver_name, logPath=str(self.log_file), msg=0)
        self.objective = 0, "Objective"
        self.model = LpProblem("Sudoku", LpMinimize)
        self.model += self.objective
        self.status = 'Pending'
        self.answer: Optional[Answer] = None
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
        self.variables = {}

        for row, column in product(board.row_range, board.column_range):
            total = lpSum(digit * self.choices[digit][row][column] for digit in self.board.digit_range)
            self.model += total == self.values[row][column], f"Unique_cell_{row}_{column}"

        # self.model += lpSum(self.choices)  == self.board.board_rows * self.board.board_columns, "ChoiceCount"

    def save(self, filename: str) -> None:
        super().save(filename)
        self.model.writeLP(filename)

    def solve(self) -> None:
        super().solve()
        self.model.solve(self.application)
        self.status = LpStatus[self.model.status]
        if self.model.status != LpStatusOptimal:
            return
        self.answer = Answer(self.board)
        for row in self.board.row_range:
            for column in self.board.column_range:
                self.answer.set_value(row, column, int(self.values[row][column].varValue))

    def get_log_details(self) -> Dict:
        return orloge.get_info_solver(self.log_file, self.application_name)
