from src.items.difference_pair import DifferencePair
from src.solvers.pulp_solver import PulpSolver


class LessThanEqualDifferencePair(DifferencePair):

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'LessThanEqualDifference'})

    def add_constraint(self, solver: PulpSolver) -> None:
        value1 = solver.values[self.c1.row][self.c1.column]
        value2 = solver.values[self.c2.row][self.c2.column]
        difference = value1 - value2
        solver.model += difference <= self.difference, f"{self.name}_upper"
        solver.model += -difference <= self.difference, f"{self.name}_lower"