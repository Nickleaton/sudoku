"""GreaterThanEqualDifferencePair."""
from pulp import LpVariable, LpInteger

from src.items.fixed_difference_pair import FixedDifferencePair
from src.solvers.pulp_solver import PulpSolver


class GreaterThanEqualDifferencePair(FixedDifferencePair):
    """Enforces a minimum difference constraint between two cells in a pair."""

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with this constraint.

        Returns:
            set[str]: A set of tags, including 'GreaterThanEqualDifference'.
        """
        return super().tags.union({'GreaterThanEqualDifference'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to ensure the difference between two cells is at least the specified value.

        Adds two constraints to the solver:

        1. An upper bound constraint that ensures the difference between the two cells
           is at least the given difference when the indicator variable is 1.
        2. A lower bound constraint that ensures the difference is at most the
           given difference when the indicator variable is 1.

        Args:
            solver (PulpSolver): The solver to add the constraints to.
        """
        big_m = self.board.maximum_digit + 1  # A large number greater than any possible cell value
        indicator = LpVariable(f"Indicator_{self.name}", 0, 1, LpInteger)  # Binary indicator variable
        value_1 = solver.values[self.cell_1.row][self.cell_1.column]  # Value of the first cell
        value_2 = solver.values[self.cell_2.row][self.cell_2.column]  # Value of the second cell
        difference = value_1 - value_2  # The difference between the two cell values

        # Upper bound constraint: difference must be at least the specified difference when the indicator is 1
        solver.model += - big_m * (1 - indicator) + self.difference * indicator <= difference, f"{self.name}_upper"

        # Lower bound constraint: difference must be at most the specified difference when the indicator is 1
        solver.model += difference <= - self.difference * (1 - indicator) + big_m * indicator, f"{self.name}_lower"
