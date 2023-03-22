import logging
from pathlib import Path
from typing import Optional

from src.commands.simple_command import SimpleCommand
from src.solvers.pulp_solver import PulpSolver


class LPCommand(SimpleCommand):

    def __init__(self, config_filename: Path):
        super().__init__(config_filename)
        self.solver: Optional[PulpSolver] = None

    def process(self) -> None:
        logging.info(f"Produce LP File {self.config_filename}")
        super().process()
        assert self.problem is not None
        assert self.board is not None
        log_file = Path("output/logs/lp") / Path(self.name + ".log")
        self.solver = PulpSolver(self.board, self.name, log_file)  # Todo
        self.problem.add_constraint(self.solver)
        self.problem.bookkeeping()
        self.problem.add_bookkeeping_constraint(self.solver)

