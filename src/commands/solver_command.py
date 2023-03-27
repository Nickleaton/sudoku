""" Base for different solvers """
import logging
from pathlib import Path
from typing import Optional

from src.commands.command import Command
from src.commands.simple_command import SimpleCommand
from src.items.solution import Solution
from src.solvers.pulp_solver import PulpSolver


class SolverCommand(SimpleCommand):

    def __init__(self, log_file_name: Path):
        """ Construct a solver
        :param log_file_name: Name of the file to write the log too
        """
        super().__init__()
        self.log_file_name = log_file_name
        self.solver: Optional[PulpSolver] = None
        self.solution: Optional[Solution] = None
        self.output: Optional[str] = None

    def execute(self) -> None:
        """
        Solve the puzzle.
        1. Bookkeep to remove obvious invalid choices
        2. Add any bookkeeping constraints.
        3. Solve
        4. Output the solution
        """
        assert self.parent.board is not None
        assert self.parent.problem is not None
        logging.info(f"Solving problem {self.parent.problem.name}")
        super().execute()
        Command.check_directory(self.log_file_name)
        self.solver = PulpSolver(self.parent.board, self.parent.problem.name, self.log_file_name)
        self.parent.problem.add_constraint(self.solver)
        self.parent.problem.bookkeeping()
        self.parent.problem.add_bookkeeping_constraint(self.solver)
        self.solver.solve()
        self.solution = self.solver.answer
        self.output = str(self.solution)

