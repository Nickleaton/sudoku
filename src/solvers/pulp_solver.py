import sys
from enum import Enum
from io import StringIO
from itertools import product
from pathlib import Path
from typing import Optional, Any, Dict

from pulp import LpVariable, LpInteger, LpProblem, LpMinimize, LpStatus, lpSum, getSolver, LpSolver

from src.items.board import Board
from src.solvers.answer import Answer
from src.solvers.solver import Solver
from src.utils.config import Config


class Status(Enum):
    NOT_SOLVED = "Not Solved"
    OPTIMAL = "Optimal"
    INFEASIBLE = "Infeasible"
    UNBOUNDED = "Unbounded"
    UNDEFINED = "Undefined"


config = Config()


class PulpSolver(Solver):  # pylint: disable=too-many-instance-attributes

    def __init__(self, board: Board, name: str, solver_name: str = 'PULP_CBC_CMD'):
        """Initializes the PulpSolver with a board and solver configuration.

        Args:
            board (Board): The game board containing the constraints.
            name (str): The name of the solver instance.
            solver_name (str): The name of the solver to use (default is 'PULP_CBC_CMD').
        """
        super().__init__(board)

        # Names
        self.name: str = name
        self.solver_name: str = solver_name
        self.application_name = 'CBC' if solver_name == 'PULP_CBC_CMD' else solver_name

        # Results
        self.status: Status = Status.NOT_SOLVED
        self.log: Optional[str] = None

        # Model
        self.model: LpProblem = LpProblem("Sudoku", LpMinimize)
        self.model += 0, "DummyObjective"

        # Create the basic model framework
        self.variables: Dict[Any, LpVariable] = {}
        self.choices: Dict[Any, LpVariable] = LpVariable.dicts("Choice",
                                        (board.digit_range, board.row_range, board.column_range),
                                        0,
                                        1,
                                        LpInteger
                                        )
        self.values: Dict[Any, LpVariable] = LpVariable.dicts("Values",
                                       (board.row_range, board.column_range),
                                       1,
                                       board.maximum_digit,
                                       LpInteger
                                       )

        self.parity: Dict[Any, LpVariable] = LpVariable.dicts("Parity",
                                       (board.row_range, board.column_range),
                                       0,
                                       1,
                                       LpInteger
                                       )

        self.levels: Dict[Any, LpVariable] = LpVariable.dicts("Low",
                                    (board.row_range, board.column_range, board.levels),
                                    0,
                                    1,
                                    LpInteger
                                    )

        self.modulos: Dict[Any, LpVariable] = LpVariable.dicts("Low",
                                    (board.row_range, board.column_range, board.modulos),
                                    0,
                                    1,
                                    LpInteger
                                    )

        self.prime: Dict[Any, LpVariable] = LpVariable.dicts("Low",
                                    (board.row_range, board.column_range, board.primes),
                                    0,
                                    1,
                                    LpInteger
                                    )

        for row, column in product(board.row_range, board.column_range):
            total = lpSum(digit * self.choices[digit][row][column] for digit in self.board.digit_range)
            self.model += total == self.values[row][column], f"Unique_cell_{row}_{column}"

    def save_lp(self, filename: Path | str) -> None:
        """Saves the model as an LP file.

        Args:
            filename (Path | str): The filename or Path object where the LP file should be saved.
        """
        super().save_lp(filename)
        if isinstance(filename, Path):
            self.model.writeLP(filename.name)
        else:
            self.model.writeLP(filename)

    def save_mps(self, filename: Path | str) -> None:
        """Saves the model as an MPS file.

        Args:
            filename (Path | str): The filename or Path object where the MPS file should be saved.
        """
        super().save_mps(filename)
        if isinstance(filename, Path):
            self.model.writeMPS(filename.name)
        else:
            self.model.writeMPS(filename)

    def solve(self) -> None:
        """Solves the model and updates the status.

        The method captures the log output during the solving process and stores it in the `log` attribute.
        """
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
