import logging
from typing import Optional

from src.commands.simple_command import SimpleCommand
from src.items.solution import Solution
from src.solvers.pulp_solver import PulpSolver


class VerifyCommand(SimpleCommand):

    def __init__(self, config_filename: str, output_filename: str):
        super().__init__(config_filename, output_filename)
        self.solver: Optional[PulpSolver] = None
        self.solution: Optional[Solution] = None
        self.output: Optional[str] = None

    def process(self) -> None:
        logging.info(f"Solving File {self.config_filename}")
        super().process()
        assert self.board is not None
        assert self.problem is not None
        self.solver = PulpSolver(self.board, self.name, "output/logs/verify")
        self.problem.add_constraint(self.solver, None, None)
        self.problem.bookkeeping()
        self.problem.add_bookkeeping_contraint(self.solver, None, None)
        self.solver.solve()
        self.solution = self.solver.answer
        self.output = str(self.solution)
