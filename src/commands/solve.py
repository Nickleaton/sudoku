import logging
from typing import Optional

from src.commands.command import Command
from src.items.solution import Solution
from src.solvers.pulp_solver import PulpSolver


class Solve(Command):

    def __init__(self, config_filename: str, output_filename: str):
        super().__init__(config_filename, output_filename)
        self.solver: Optional[PulpSolver] = None
        self.solution: Optional[Solution] = None
        self.output: Optional[str] = None

    def process(self) -> None:
        assert self.board is not None
        assert self.problem is not None
        logging.info(f"Produce LP File {self.config_filename}")
        super().process()
        self.solver = PulpSolver(self.board)
        self.problem.add_variables(self.board, self.solver)
        self.problem.add_constraint(self.solver)
        self.solver.solve()
        self.solution = self.solver.solution
        self.output = str(self.solution)
