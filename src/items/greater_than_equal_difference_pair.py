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
        value_1 = solver.values[self.cell_1.row][self.cell_1.column]
        value_2 = solver.values[self.cell_2.row][self.cell_2.column]
        difference = value_1 - value_2
        solver.model += - big_m * (1 - indicator) + self.difference * indicator <= difference, f"{self.name}_upper"
        solver.model += difference <= - self.difference * (1 - indicator) + big_m * indicator, f"{self.name}_lower"
