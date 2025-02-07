"""Solver."""
import logging
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from pulp import getSolver  # noqa: I001
from pulp import LpMinimize  # noqa: I001
from pulp import LpProblem  # noqa: I001
from pulp import LpSolver  # noqa: I001
from pulp import LpStatus  # noqa: I001

from src.board.board import Board
from src.solvers.answer import Answer
from src.solvers.solver_status import SolverStatus
from src.solvers.variables import Variables  # noqa: I001
from src.solvers.variables import VariableSet  # noqa: I001
from src.utils.config import Config

config = Config()


class Solver:
    """Solver class that manages the solving of a puzzle using a given board and line representation."""

    def __init__(self, board: Board, name: str, solver_name: str = 'PULP_CBC_CMD'):
        """Initialize the Solver with the given board, solver name, and application name.

        Args:
            board (Board): The board object representing the puzzle layout.
            name (str): Name for the solver instance.
            solver_name (str): Solver name, default is 'PULP_CBC_CMD'.
        """
        self.board: Board = board
        self.answer: Answer = Answer(self.board)
        self.name: str = name
        self.solver_name: str = solver_name
        self.application_name = 'CBC' if solver_name == 'PULP_CBC_CMD' else solver_name

        self.status: SolverStatus = SolverStatus.not_solved
        self.log: str | None = None

        # TODO: get the types of variables from the constraints
        self.variables: Variables = Variables(board, [VariableSet.choice, VariableSet.number])

        self.model: LpProblem = LpProblem(self.name, LpMinimize)
        self.model += 0, 'DummyObjective'

    def save_lp(self, filename: Path | str) -> None:
        """Save the puzzle model in LP (Linear Programming) format.

        Args:
            filename (Path | str): The config_file or name of the file_path to save the LP format.
        """
        if isinstance(filename, Path):
            self.model.writeLP(filename.name)
        else:
            self.model.writeLP(filename)

    def save_mps(self, filename: Path | str) -> None:
        """Save the puzzle model in MPS (Mathematical Programming System) format.

        Args:
            filename (Path | str): The config_file or name of the file_path to save the MPS format.
        """
        if isinstance(filename, Path):
            self.model.writeMPS(filename.name)
        else:
            self.model.writeMPS(filename)

    def solve(self) -> None:
        """Solve the puzzle using the specified solver and update the solution status."""
        application: LpSolver = getSolver(self.solver_name, msg=1)
        log_output = StringIO()
        try:
            with redirect_stdout(log_output):
                self.model.solve(application)
        except Exception as exp:
            # Log the exception for better traceability
            logging.error(f'Error occurred during solving: {exp!s}', exc_info=True)
            self.status = SolverStatus(LpStatus.INFEASIBLE)  # or another status
            self.log = f'Error occurred: {exp!s}'
            return  # Exit early if there's an error
        self.status = SolverStatus(LpStatus[self.model.status])
        self.log = log_output.getvalue()
