from typing import List

from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class DifferencePair(Pair):

    @property
    def difference(self) -> int:
        return 0

    @property
    def rules(self) -> List[Rule]:
        return []

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Difference'})

    def add_constraint(self, solver: PulpSolver) -> None:
        total = solver.values[self.c1.row][self.c1.column] + solver.values[self.c2.row][self.c2.column]
        solver.model += total == self.difference, self.name
