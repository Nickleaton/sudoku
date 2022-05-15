import logging

from src.commands.command import Command
from src.solvers.pulp_solver import PulpSolver


class LP(Command):

    def __init__(self, config_filename: str, output_filename: str):
        super().__init__(config_filename, output_filename)
        self.solver = None

    def process(self) -> None:
        logging.info(f"Produce LP File {self.config_filename}")
        super().process()
        self.solver = PulpSolver(self.board)
        self.problem.add_variables(self.board, self.solver)
        self.problem.add_constraint(self.solver)

    def write(self) -> None:
        self.check_directory()
        logging.info(f"Writing output to {self.output_filename}")
        self.solver.save(self.output_filename)
