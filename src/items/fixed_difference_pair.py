"""FixedDifferencePair."""
from typing import List, Dict

from pulp import LpElement

from src.items.fixed_pair import FixedPair
from src.solvers.formulations import Formulations
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class FixedDifferencePair(FixedPair):
    """Represents a fixed difference constraint between two cells.

    The digits in those cells have a fixed difference.
    """

    @property
    def difference(self) -> int:
        """Returns the fixed difference between the digits of the two cells.

        Returns:
            int: The fixed difference between the two cells.
        """
        return self.value

    @property
    def rules(self) -> List[Rule]:
        """Returns the rules associated with the FixedDifferencePair item.

        Returns:
            List[Rule]: A list of rules that describe the fixed difference constraint between two cells.
        """
        return [
            Rule(
                self.__class__.__name__,
                1,
                (
                    "A white dot between two cells means that the digits in those cells "
                    "have a fixed difference."
                )
            )
        ]

    @property
    def tags(self) -> set[str]:
        """Returns the tags associated with the FixedDifferencePair item.

        Returns:
            set[str]: A set of tags, including 'Difference', to categorize the item.
        """
        return super().tags.union({'Difference'})

    def target(self, solver: PulpSolver) -> LpElement:
        """Calculate the absolute difference between the values in the two cells.

        Args:
            solver (PulpSolver): The solver instance used to access the variable values.

        Returns:
            LpElement: The absolute difference between the two cell values, formulated as a constraint.
        """
        v1 = solver.values[self.cell_1.row][self.cell_1.column]
        v2 = solver.values[self.cell_2.row][self.cell_2.column]
        return Formulations.abs(solver.model, v1, v2, self.board.maximum_digit + 1)

    def css(self) -> Dict:
        """Return the CSS styles for rendering the FixedDifferencePair visually.

        Returns:
            Dict: A dictionary containing the CSS styles for the FixedDifferencePair.
        """
        return {
            '.FixedDifferencePair': {
                'fill': 'white',
                'stroke-width': 1,
                'stroke': 'black'
            }
        }
