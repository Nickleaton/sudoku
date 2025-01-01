"""VariableProductPair."""

from pulp import LpElement

from src.items.variable_pair import VariablePair
from src.solvers.constraint_utilities import ConstraintUtilities
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.variable_type import VariableType


class VariableProductPair(VariablePair):
    """Represents start pair of variables with start fixed product in start Sudoku-like puzzle."""

    @property
    def rules(self) -> list[Rule]:
        """Get the rules associated with this value_variable product pair.

        Returns:
            list[Rule]: A list of rules describing the product constraints.
        """
        rule_text: str = 'A red dot between two cells means that the digits in those cells have a fixed product'
        return [Rule(self.__class__.__name__, 1, rule_text)]

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with this value_variable product pair.

        Returns:
            set[str]: A set of tags for identifying this type of value_variable pair.
        """
        return super().tags.union({'Product'})

    def target(self, solver: PulpSolver) -> LpElement | None:
        """Calculate the target expression for the value_variable product pair.

        Args:
            solver (PulpSolver): The solver instance to use for value_variable constraints.

        Returns:
            LpElement | None: The expression representing the target constraints based
                                 on the logarithm of cell value_list,or None if unable to calculate.
        """
        x1 = ConstraintUtilities.log10_cell(solver, self.cell1)
        x2 = ConstraintUtilities.log10_cell(solver, self.cell2)
        return x1 + x2

    def variable_type(self) -> VariableType:
        """Get the value_variable type for this value_variable product pair.

        Returns:
            VariableType: The type of value_variable, which is log_integer for this pair.
        """
        return VariableType.log_integer

    def css(self) -> dict:
        """Get the CSS styles for this value_variable product pair.

        Returns:
            dict: A dictionary containing CSS styles for visual representation.
        """
        return {
            '.FixedProductPair': {
                'fill': 'red',
                'stroke-width': 1,
                'stroke': 'black',
            },
        }
