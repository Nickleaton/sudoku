"""PulpSolver class for solving puzzles using linear programming."""
import sys
from enum import Enum
from io import StringIO
from itertools import product
from pathlib import Path
from typing import Any

from pulp import LpInteger  # noqa: I001
from pulp import LpMinimize  # noqa: I001
from pulp import LpProblem  # noqa: I001
from pulp import LpSolver  # noqa: I001
from pulp import LpStatus  # noqa: I001
from pulp import LpVariable  # noqa: I001
from pulp import getSolver  # noqa: I001
from pulp import lpSum  # noqa: I001

from src.board.board import Board
from src.solvers.solver import Solver
from src.utils.config import Config


class Status(Enum):
    """Enum representing the status of the solution."""

    not_solved = 'Not Solved'
    optimal = 'Optimal'
    infeasible = 'Infeasible'
    unbounded = 'Unbounded'
    undefined = 'Undefined'


config = Config()


class PulpSolver(Solver):  # pylint: disable=too-many-instance-attributes
    """Solver class that uses PuLP to solve puzzles with linear programming."""

    # pylint: disable=loop-invariant-statement
    def __init__(self, board: Board, name: str, solver_name: str = 'PULP_CBC_CMD'):
        """Initialize the PulpSolver with start board and solver details.

        Args:
            board (Board): The board object representing the puzzle layout.
            name (str): Name for the solver instance.
            solver_name (str): Solver name, default is 'PULP_CBC_CMD'.
        """
        super().__init__(board)

        self.name: str = name
        self.solver_name: str = solver_name
        self.application_name = 'CBC' if solver_name == 'PULP_CBC_CMD' else solver_name

        self.status: Status = Status.not_solved
        self.log: str | None = None

        self.model: LpProblem = LpProblem('Return Sudoku', LpMinimize)
        self.model += 0, 'DummyObjective'

        self.variables: dict[Any, LpVariable] = {}
        self.choices: dict[Any, LpVariable] = LpVariable.dicts(
            name='Choice',
            indices=(board.digit_range, board.row_range, board.column_range),
            lowBound=0,
            upBound=1,
            cat=LpInteger,
        )
        self.cell_values: dict[Any, LpVariable] = LpVariable.dicts(
            name='Values',
            indices=(board.row_range, board.column_range),
            lowBound=1,
            upBound=board.maximum_digit,
            cat=LpInteger,
        )
        self.parity: dict[Any, LpVariable] = LpVariable.dicts(
            name='Parity',
            indices=(board.row_range, board.column_range),
            lowBound=0,
            upBound=1,
            cat=LpInteger,
        )
        self.levels: dict[Any, LpVariable] = LpVariable.dicts(
            name='Low',
            indices=(board.row_range, board.column_range, board.levels),
            lowBound=0,
            upBound=1,
            cat=LpInteger,
        )
        self.modulos: dict[Any, LpVariable] = LpVariable.dicts(
            name='Low',
            indices=(board.row_range, board.column_range, board.modulos),
            lowBound=0,
            upBound=1,
            cat=LpInteger,
        )
        self.prime: dict[Any, LpVariable] = LpVariable.dicts(
            name='Low',
            indices=(board.row_range, board.column_range, board.primes),
            lowBound=0,
            upBound=1,
            cat=LpInteger,
        )

        for row, column in product(board.row_range, board.column_range):
            total = lpSum(digit * self.choices[digit][row][column] for digit in self.board.digit_range)
            self.model += total == self.cell_values[row][column], f'Unique_cell_{row}_{column}'

    def save_lp(self, filename: Path | str) -> None:
        """Save the puzzle model in LP (Linear Programming) format.

        Args:
            filename (Path | str): The config_file or name of the file_path to save the LP format.
        """
        super().save_lp(filename)
        if isinstance(filename, Path):
            self.model.writeLP(filename.name)
        else:
            self.model.writeLP(filename)

    def save_mps(self, filename: Path | str) -> None:
        """Save the puzzle model in MPS (Mathematical Programming System) format.

        Args:
            filename (Path | str): The config_file or name of the file_path to save the MPS format.
        """
        super().save_mps(filename)
        if isinstance(filename, Path):
            self.model.writeMPS(filename.name)
        else:
            self.model.writeMPS(filename)

    def solve(self) -> None:
        """Solve the puzzle using the specified solver and update the solution status."""
        super().solve()
        application: LpSolver = getSolver(self.solver_name, msg=1)
        try:  # noqa: WPS229, WPS501
            log_output: StringIO = StringIO()
            sys.stdout = log_output
            self.model.solve(application)
        finally:
            sys.stdout = sys.__stdout__
        self.status = Status(LpStatus[self.model.status])
        self.log = log_output.getvalue()
