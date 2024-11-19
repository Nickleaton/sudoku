"""VariableProductPair."""

from pulp import LpElement

from src.items.variable_pair import VariablePair
from src.solvers.constraint_utilities import ConstraintUtilities
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.variable_type import VariableType


class VariableProductPair(VariablePair):
    """Represents a pair of variables with a fixed product in a Sudoku-like puzzle."""

    @property
    def rules(self) -> list[Rule]:
        """Get the rules associated with this variable product pair.

        Returns:
            list[Rule]: A list of rules describing the product constraints.
        """
        return [
            Rule(
                self.__class__.__name__,
                1,
                (
                    "A red dot between two cells means that the digits in those cells "
                    "have a fixed product"
                )
            )
        ]

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with this variable product pair.

        Returns:
            set[str]: A set of tags for identifying this type of variable pair.
        """
        return super().tags.union({'Product'})

    def target(self, solver: PulpSolver) -> LpElement |  None:
        """Calculate the target expression for the variable product pair.

        Args:
            solver (PulpSolver): The solver instance to use for variable constraints.

        Returns:
            LpElement | None: The expression representing the target constraints based
                                 on the logarithm of cell values,or None if unable to calculate.
        """
        x1 = ConstraintUtilities.log10_cell(solver, self.cell_1)
        x2 = ConstraintUtilities.log10_cell(solver, self.cell_2)
        return x1 + x2

    def variable_type(self) -> VariableType:
        """Get the variable type for this variable product pair.

        Returns:
            VariableType: The type of variable, which is LOG_INTEGER for this pair.
        """
        return VariableType.LOG_INTEGER

    def css(self) -> dict:
        """Get the CSS styles for this variable product pair.

        Returns:
            dict: A dictionary containing CSS styles for visual representation.
        """
        return {
            '.FixedProductPair': {
                'fill': 'red',
                'stroke-width': 1,
                'stroke': 'black'
            }
        }
