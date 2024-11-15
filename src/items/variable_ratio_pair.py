"""VariableRatioPair."""
from math import ceil, log10
from typing import List, Dict

from pulp import LpElement

from src.items.variable_pair import VariablePair
from src.solvers.constraint_utilities import ConstraintUtilities
from src.solvers.formulations import Formulations
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.variable_type import VariableType


class VariableRatioPair(VariablePair):
    """Represents a pair of variables with a fixed ratio in a Sudoku-like puzzle."""

    @property
    def rules(self) -> List[Rule]:
        """Get the rules associated with this variable ratio pair.

        Returns:
            List[Rule]: A list of rules describing the ratio constraints.
        """
        return [
            Rule(
                self.__class__.__name__,
                1,
                (
                    "A black dot between two cells means that one of the digits in those cells "
                    "have a fixed ratio. The ratio is not necessarily an integer"
                )
            )
        ]

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with this variable ratio pair.

        Returns:
            set[str]: A set of tags for identifying this type of variable pair.
        """
        return super().tags.union({'Ratio'})

    def variable_type(self) -> VariableType:
        """Get the variable type for this variable ratio pair.

        Returns:
            VariableType: The type of variable, which is LOG_FLOAT for this pair.
        """
        return VariableType.LOG_FLOAT

    def target(self, solver: PulpSolver) -> LpElement:
        """Calculate the target expression for the variable ratio pair.

        Args:
            solver (PulpSolver): The solver instance to use for variable constraints.

        Returns:
            LpElement: The expression representing the target constraints based on the logarithm of cell values.
        """
        limit = ceil(log10(self.board.maximum_digit)) + 1
        x1 = ConstraintUtilities.log10_cell(solver, self.cell_1)
        x2 = ConstraintUtilities.log10_cell(solver, self.cell_2)
        return Formulations.abs(
            solver.model,
            x1,
            x2,
            limit
        )

    def css(self) -> Dict:
        """Get the CSS styles for this variable ratio pair.

        Returns:
            Dict: A dictionary containing CSS styles for visual representation.
        """
        return {
            '.FixedRatioPair': {
                'fill': 'black',
                'stroke-width': 1,
                'stroke': 'black'
            }
        }
