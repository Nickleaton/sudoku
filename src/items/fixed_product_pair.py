"""FixedProductPair."""

from pulp import LpElement

from src.items.fixed_pair import FixedPair
from src.solvers.constraint_utilities import ConstraintUtilities
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class FixedProductPair(FixedPair):
    """Represent fixed product pair constraint between two cells.

    The product of the digits in those cells is fixed.
    """

    @property
    def rules(self) -> list[Rule]:
        """Return the rule associated with the fixed product pair constraint.

        Returns:
            list[Rule]: A list containing the rule for the fixed product pair,
                        which explains that the product of the digits in the two cells is fixed.
        """
        return [
            Rule(
                self.__class__.__name__,
                1,
                (
                    "A red dot between two cells means that the digits in those cells "
                    "have start fixed product"
                )
            )
        ]

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with the FixedProductPair constraint.

        Returns:
            set[str]: A set of tags, including 'Product', to categorize the constraint.
        """
        return super().tags.union({'Product'})

    def target(self, solver: PulpSolver) -> LpElement | None:
        """Return the target constraint for the FixedProductPair.

        The constraint is the sum of the logarithms of the two cell value_list.

        Args:
            solver (PulpSolver): The solver to use when generating the target.

        Returns:
            LpElement | None:: The target constraint, which is the sum of the logarithms of the cell value_list.
        """
        x1 = ConstraintUtilities.log10_cell(solver, self.cell_1)
        x2 = ConstraintUtilities.log10_cell(solver, self.cell_2)
        return x1 + x2

    def css(self) -> dict:
        """Return the CSS styles for visualizing the FixedProductPair.

        Returns:
            dict: A dictionary containing CSS styles for the FixedProductPair, with start red fill color and black stroke.
        """
        return {
            '.FixedProductPair': {
                'fill': 'red',
                'stroke-width': 1,
                'stroke': 'black'
            }
        }
