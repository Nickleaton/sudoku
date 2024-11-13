from src.items.difference_pair import DifferencePair
from src.solvers.pulp_solver import PulpSolver


class LessThanEqualDifferencePair(DifferencePair):

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'LessThanEqualDifference'})

    def add_constraint(self, solver: PulpSolver) -> None:
        value1 = solver.values[self.cell_1.row][self.cell_1.column]
        value2 = solver.values[self.cell_2.row][self.cell_2.column]
        diff = value1 - value2
        solver.model += diff <= self.difference, f"{self.name}_upper"
        solver.model += -diff <= self.difference, f"{self.name}_lower"

    @property
    def difference(self) -> int:
        return 0
