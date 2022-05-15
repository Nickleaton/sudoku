import logging

from src.commands.command import Command
from src.solvers.pulp_solver import PulpSolver


class Solve(Command):

    def __init__(self, config_filename: str, output_filename: str):
        super().__init__(config_filename, output_filename)
        self.solver = None
        self.solution = None
        self.output = None

    def process(self) -> None:
        logging.info(f"Produce LP File {self.config_filename}")
        super().process()
        self.solver = PulpSolver(self.board)
        self.problem.add_variables(self.board, self.solver)
        self.problem.add_constraint(self.solver)
        self.solver.solve()
        self.solution = self.solver.solution
        self.output = str(self.solution)