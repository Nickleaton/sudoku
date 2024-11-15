"""VariableDifferencePair."""
from typing import List, Dict

from pulp import LpElement

from src.items.variable_pair import VariablePair
from src.solvers.formulations import Formulations
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.variable_type import VariableType


class VariableDifferencePair(VariablePair):
    """Represents a pair of cells with a fixed difference indicated by a white dot."""

    @property
    def rules(self) -> List[Rule]:
        """Get the rules associated with the VariableDifferencePair.

        Returns:
            List[Rule]: A list of rules describing the VariableDifferencePair constraints.
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

    def variable_type(self) -> VariableType:
        """Define the type of variable for this pair.

        Returns:
            VariableType: The type of the variable, which is an integer.
        """
        return VariableType.INT

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with the VariableDifferencePair.

        Returns:
            set[str]: A set of tags including 'Difference'.
        """
        return super().tags.union({'Difference'})

    def target(self, solver: PulpSolver) -> LpElement:
        """Calculate the absolute difference between the values of the pair in the solver.

        Args:
            solver (PulpSolver): The solver managing the constraints.

        Returns:
            LpElement: The absolute difference between the values of the two cells.
        """
        v1 = solver.values[self.cell_1.row][self.cell_1.column]
        v2 = solver.values[self.cell_2.row][self.cell_2.column]
        return Formulations.abs(solver.model, v1, v2, self.board.maximum_digit + 1)

    def css(self) -> Dict:
        """Define the CSS styles for rendering VariableDifferencePair glyphs.

        Returns:
            Dict: A dictionary of CSS properties.
        """
        return {
            '.FixedDifferencePair': {
                'fill': 'white',
                'stroke-width': 1,
                'stroke': 'black'
            }
        }

