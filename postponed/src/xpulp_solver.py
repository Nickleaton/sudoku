"""Solver class for solving puzzles using linear programming."""
import sys
from io import StringIO
from pathlib import Path

from pulp import LpMinimize  # noqa: I001
from pulp import LpProblem  # noqa: I001
from pulp import LpSolver  # noqa: I001
from pulp import LpStatus  # noqa: I001
from pulp import getSolver  # noqa: I001

from src.board.board import Board
from src.solvers.solver import Solver
from src.solvers.solver_status import SolverStatus
from src.variables import Variables, VariableSet
from src.utils.config import Config

config = Config()


class PulpSolver(Solver):  # pylint: disable=too-many-instance-attributes
    """Solver class that uses PuLP to solve puzzles with linear programming."""

    # pylint: disable=loop-invariant-statement
    def __init__(self, board: Board, name: str, solver_name: str = 'PULP_CBC_CMD'):
        """Initialize the Solver with start_location board and solver details.

        Args:
            board (Board): The board object representing the puzzle layout.
            name (str): Name for the solver instance.
            solver_name (str): Solver name, default is 'PULP_CBC_CMD'.
        """
        super().__init__(board)

        self.name: str = name
        self.solver_name: str = solver_name
        self.application_name = 'CBC' if solver_name == 'PULP_CBC_CMD' else solver_name

        self.status: SolverStatus = SolverStatus.not_solved
        self.log: str | None = None

        # TODO get the types of variables from the constraints
        self.variables: Variables = Variables(board, [VariableSet.choice, VariableSet.number])

        self.model: LpProblem = LpProblem(self.name, LpMinimize)
        self.model += 0, 'DummyObjective'

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
        self.status = SolverStatus(LpStatus[self.model.status])
        self.log = log_output.getvalue()
