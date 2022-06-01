import logging
import re
from typing import Optional

from src.commands.simple_command import SimpleCommand
from src.solvers.pulp_solver import PulpSolver


class LPCommand(SimpleCommand):

    def __init__(self, config_filename: str, output_filename: str):
        super().__init__(config_filename, output_filename)
        self.solver: Optional[PulpSolver] = None

    def process(self) -> None:
        logging.info(f"Produce LP File {self.config_filename}")
        super().process()
        assert self.problem is not None
        assert self.board is not None
        self.solver = PulpSolver(self.board, self.name, "output/logs/lp")
        self.problem.add_constraint(self.solver)
        self.problem.bookkeeping()
        self.problem.add_bookkeeping_contraint(self.solver)

    def write(self) -> None:
        assert self.solver is not None
        assert self.output_filename is not None
        self.check_directory()
        logging.info(f"Writing output to {self.output_filename}")
        self.solver.save(self.output_filename)
