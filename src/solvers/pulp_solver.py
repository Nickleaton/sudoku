"""PulpSolver class for solving puzzles using linear programming."""
import sys
from enum import Enum
from io import StringIO
from itertools import product
from pathlib import Path
from typing import Any

from pulp import LpVariable, LpInteger, LpProblem, LpMinimize, LpStatus, lpSum, getSolver, LpSolver

from src.items.board import Board
from src.solvers.solver import Solver
from src.utils.config import Config


class Status(Enum):
    """Enum representing the status of the solution."""

    NOT_SOLVED = "Not Solved"
    OPTIMAL = "Optimal"
    INFEASIBLE = "Infeasible"
    UNBOUNDED = "Unbounded"
    UNDEFINED = "Undefined"


config = Config()


class PulpSolver(Solver):  # pylint: disable=too-many-instance-attributes
    """Solver class that uses PuLP to solve puzzles with linear programming."""

    # pylint: disable=loop-invariant-statement
    def __init__(self, board: Board, name: str, solver_name: str = 'PULP_CBC_CMD'):
        """Initialize the PulpSolver with a board and solver details.

        Args:
            board (Board): The board object representing the puzzle layout.
            name (str): Name for the solver instance.
            solver_name (str): Solver name, default is 'PULP_CBC_CMD'.
        """
        super().__init__(board)

        self.name: str = name
        self.solver_name: str = solver_name
        self.application_name = 'CBC' if solver_name == 'PULP_CBC_CMD' else solver_name

        self.status: Status = Status.NOT_SOLVED
        self.log: str | None = None

        self.model: LpProblem = LpProblem("Sudoku", LpMinimize)
        self.model += 0, "DummyObjective"

        self.variables: dict[Any, LpVariable] = {}
        self.choices: dict[Any, LpVariable] = LpVariable.dicts(
            "Choice",
            (board.digit_range, board.row_range, board.column_range),
            0,
            1,
            LpInteger
        )
        self.values: dict[Any, LpVariable] = LpVariable.dicts(
            "Values",
            (board.row_range, board.column_range),
            1,
            board.maximum_digit,
            LpInteger
        )
        self.parity: dict[Any, LpVariable] = LpVariable.dicts(
            "Parity",
            (board.row_range, board.column_range),
            0,
            1,
            LpInteger
        )
        self.levels: dict[Any, LpVariable] = LpVariable.dicts(
            "Low",
            (board.row_range, board.column_range, board.levels),
            0,
            1,
            LpInteger
        )
        self.modulos: dict[Any, LpVariable] = LpVariable.dicts(
            "Low",
            (board.row_range, board.column_range, board.modulos),
            0,
            1,
            LpInteger
        )
        self.prime: dict[Any, LpVariable] = LpVariable.dicts(
            "Low",
            (board.row_range, board.column_range, board.primes),
            0,
            1,
            LpInteger
        )

        for row, column in product(board.row_range, board.column_range):
            total = lpSum(digit * self.choices[digit][row][column] for digit in self.board.digit_range)
            self.model += total == self.values[row][column], f"Unique_cell_{row}_{column}"

    def save_lp(self, filename: Path | str) -> None:
        """Save the puzzle model in LP (Linear Programming) format.

        Args:
            filename (Path | str): The config_file or name of the file to save the LP format.
        """
        super().save_lp(filename)
        if isinstance(filename, Path):
            self.model.writeLP(filename.name)
        else:
            self.model.writeLP(filename)

    def save_mps(self, filename: Path | str) -> None:
        """Save the puzzle model in MPS (Mathematical Programming System) format.

        Args:
            filename (Path | str): The config_file or name of the file to save the MPS format.
        """
        super().save_mps(filename)
        if isinstance(filename, Path):
            self.model.writeMPS(filename.name)
        else:
            self.model.writeMPS(filename)

    def solve(self) -> None:
        """Solve the puzzle using the specified solver and updates the solution status."""
        super().solve()
        log_output: StringIO = StringIO()
        try:
            sys.stdout = log_output
            application: LpSolver = getSolver(self.solver_name, msg=1)
            self.model.solve(application)
        finally:
            sys.stdout = sys.__stdout__
        self.status = Status(LpStatus[self.model.status])
        self.log = log_output.getvalue()
