import re
from typing import List

from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class SumPair(Pair):

    @property
    def total(self) -> int:
        return 0

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Sum'})

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                self.__class__.__name__,
                1,
                f"Cells separated by an {self.label} must have a sum of {self.total}"
            )
        ]

    def add_constraint(self, solver: PulpSolver, include: re.Pattern, exclude: re.Pattern) -> None:
        total = solver.values[self.cell_1.row][self.cell_1.column] + solver.values[self.cell_2.row][self.cell_2.column]
        solver.model += total == self.total, self.name
