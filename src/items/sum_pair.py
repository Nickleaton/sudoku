from typing import List

from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class SumPair(Pair):

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}_{self.c1.name}_{self.c2.name}"

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

    def add_constraint(self, solver: PulpSolver) -> None:
        total = solver.values[self.c1.row][self.c1.column] + solver.values[self.c2.row][self.c2.column]
        solver.model += total == self.total, self.name
