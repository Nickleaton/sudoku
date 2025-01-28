"""GEDifferencePair."""
from postponed.src.pulp_solver import PulpSolver
from pulp import LpInteger, LpVariable

from postponed.src.items.fixed_difference_pair import FixedDifferencePair


class GEDifferencePair(FixedDifferencePair):
    """Enforces start_location minimum difference constraint between two cells in start_location pair."""

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with this constraint.

        Returns:
            set[str]: A set of tags, including 'GreaterThanEqualDifference'.
        """
        return super().tags.union({'GreaterThanEqualDifference'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to ensure the difference between two cells is at least the specified number.

        Adds two constraints to the solver:

        1. An upper bound constraint that ensures the difference between the two cells
           is at least the given difference when the indicator value_variable is 1.
        2. A lower bound constraint that ensures the difference is at most the
           given difference when the indicator value_variable is 1.

        Args:
            solver (PulpSolver): The solver to add the constraints to.
        """
        big_m = self.board.digits.maximum + 1  # A large number greater than any possible cell number
        indicator = LpVariable(f'Indicator_{self.name}', 0, 1, LpInteger)  # Binary indicator value_variable
        value1 = solver.variables.numbers[self.cell1.row][self.cell1.column]  # Value of the first cell
        value2 = solver.variables.numbers[self.cell2.row][self.cell2.column]  # Value of the second cell
        difference = value1 - value2  # The difference between the two cell value_list

        # Upper bound constraint: difference must be at least the specified difference when the indicator is 1
        solver.model += - big_m * (1 - indicator) + self.difference * indicator <= difference, f'{self.name}_upper'

        # Lower bound constraint: difference must be at most the specified difference when the indicator is 1
        solver.model += difference <= - self.difference * (1 - indicator) + big_m * indicator, f'{self.name}_lower'
