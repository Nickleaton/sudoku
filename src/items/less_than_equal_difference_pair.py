from src.items.difference_pair import DifferencePair
from src.solvers.pulp_solver import PulpSolver


class LessThanEqualDifferencePair(DifferencePair):
    """Represents a pair of cells with a difference constrained by a less-than-or-equal condition."""

    @property
    def tags(self) -> set[str]:
        """Retrieve the set of tags associated with this difference pair.

        Returns:
            set[str]: The set of tags, including 'LessThanEqualDifference'.
        """
        return super().tags.union({'LessThanEqualDifference'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the solver to enforce the less-than-or-equal difference condition.

        Args:
            solver (PulpSolver): The solver to which the constraints are added.
        """
        value1 = solver.values[self.cell_1.row][self.cell_1.column]
        value2 = solver.values[self.cell_2.row][self.cell_2.column]
        diff = value1 - value2
        solver.model += diff <= self.difference, f"{self.name}_upper"
        solver.model += -diff <= self.difference, f"{self.name}_lower"

    @property
    def difference(self) -> int:
        """Retrieve the maximum allowed difference between the two cells.

        Returns:
            int: The maximum allowed difference, which is always 0 for this class.
        """
        return 0
