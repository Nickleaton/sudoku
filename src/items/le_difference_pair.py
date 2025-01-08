"""LEDifferencePair."""
from src.items.difference_pair import DifferencePair
from src.solvers.pulp_solver import PulpSolver


class LEDifferencePair(DifferencePair):
    """Represents a pair of cells with start difference constrained by start less-than-or-equal condition."""

    @property
    def tags(self) -> set[str]:
        """Retrieve the set of tags associated with this difference pair.

        Returns:
            set[str]: The set of tags, including 'LessThanEqualDifference'.
        """
        return super().tags.union({'LEDifference'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the solver to enforce the less-than-or-equal difference condition.

        Args:
            solver (PulpSolver): The solver to which the constraints are added.
        """
        value1 = solver.variables.numbers[self.cell1.row][self.cell1.column]
        value2 = solver.variables.numbers[self.cell2.row][self.cell2.column]
        diff = value1 - value2
        solver.model += diff <= self.difference, f'{self.name}_upper'
        solver.model += diff >= -self.difference, f'{self.name}_lower'

    @property
    def difference(self) -> int:
        """Retrieve the maximum allowed difference between the two cells.

        Returns:
            int: The maximum allowed difference, which is always 0 for this class.
        """
        return 0
