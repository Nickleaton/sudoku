from pulp import LpVariable, LpInteger

from src.items.difference_pair import DifferencePair
from src.solvers.pulp_solver import PulpSolver


class GreaterThanEqualDifferencePair(DifferencePair):

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'GreaterThanEqualDifference'})

    def add_constraint(self, solver: PulpSolver) -> None:
        big_m = self.board.maximum_digit + 1
        indicator = LpVariable(f"Indicator_{self.name}", 0, 1, LpInteger)
        difference = solver.values[self.c1.row][self.c1.column] - solver.values[self.c2.row][self.c2.column]
        solver.model += - big_m * (1 - indicator) + self.difference * indicator <= difference, f"{self.name}_upper"
        solver.model += difference <= - self.difference * (1 - indicator) + big_m * indicator, f"{self.name}_lower"
