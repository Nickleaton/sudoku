"""VariableSumPair."""
from typing import List, Dict

from pulp import LpElement

from src.items.variable_pair import VariablePair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.variable_type import VariableType


class VariableSumPair(VariablePair):
    """Represents a pair of cells with an associated variable that defines their sum constraint."""

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with the VariableSumPair."""
        return super().tags.union({'Sum'})

    @property
    def rules(self) -> List[Rule]:
        """Define the rule for the VariableSumPair: cells must have the same sum."""
        return [
            Rule(
                self.__class__.__name__,
                1,
                "Cells separated by a blue dot must have the same sum"
            )
        ]

    def variable_type(self) -> VariableType:
        """Return the variable type for the pair.

        Returns:
            VariableType: The type of the variable (integer).
        """
        return VariableType.INT

    def target(self, solver: PulpSolver) -> LpElement:
        """Define the target variable for the sum of the two cells in the solver.

        Args:
            solver (PulpSolver): The solver to add the target for.

        Returns:
            LpElement: The sum of the two cell values.
        """
        return solver.values[self.cell_1.row][self.cell_1.column] + solver.values[self.cell_2.row][self.cell_2.column]

    def css(self) -> Dict:
        """Return the CSS styles for the VariableSumPair."""
        return {
            '.FixedSumPair': {
                'fill': 'cyan',
                'stroke-width': 1,
                'stroke': 'black'
            }
        }
