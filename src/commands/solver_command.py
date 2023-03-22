""" Base for different solvers """
import logging
from pathlib import Path
from typing import Optional

from src.commands.command import Command
from src.commands.simple_command import SimpleCommand
from src.items.solution import Solution
from src.solvers.pulp_solver import PulpSolver


class SolverCommand(SimpleCommand):

    def __init__(self, config_filename: Path):
        super().__init__(config_filename)
        self.log_file_name = Path("output") / Path("logs") / Path(self.name) / Path("todo" + ".log")
        self.solver: Optional[PulpSolver] = None
        self.solution: Optional[Solution] = None
        self.output: Optional[str] = None

    def process(self) -> None:
        """
        Solve the puzzle.
        1. Build a board
        2. Build the constraints
        3. Bookkeep to remove obvious invalid choices
        4. Add any bookkeeping constraints.
        5. Solve
        6. Output the solution
        """
        logging.info(f"Solving File {self.config_filename}")
        super().process()
        assert self.board is not None
        assert self.problem is not None
        Command.check_directory(self.log_file_name)
        self.solver = PulpSolver(self.board, self.name, self.log_file_name)
        self.problem.add_constraint(self.solver)
        self.problem.bookkeeping()
        self.problem.add_bookkeeping_constraint(self.solver)
        self.solver.solve()
        self.solution = self.solver.answer
        self.output = str(self.solution)

