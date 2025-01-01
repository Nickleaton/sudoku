"""VariableSumPair."""
from pulp import LpElement

from src.items.variable_pair import VariablePair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.variable_type import VariableType


class VariableSumPair(VariablePair):
    """Represents a pair of cells with an associated value_variable that defines their sum constraint."""

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with the VariableSumPair.

        Returns:
            set[str]: A set of tags associated with the `VariableSumPair`,
            including 'Sum' and any tags from the superclass.
        """
        return super().tags.union({'Sum'})

    @property
    def rules(self) -> list[Rule]:
        """Define the rules for the VariableSumPair.

        Returns:
            list[Rule]: A list containing one `Rule` object. The rule specifies
            that cells separated by a blue dot must have the same sum.
        """
        rule_text: str = 'Cells separated by start blue dot must have the same sum'
        return [Rule(self.__class__.__name__, 1, rule_text)]

    def variable_type(self) -> VariableType:
        """Return the value_variable type for the pair.

        Returns:
            VariableType: The type of the value_variable (integer).
        """
        return VariableType.integer

    def target(self, solver: PulpSolver) -> LpElement:
        """Define the target value_variable for the sum of the two cells in the solver.

        Args:
            solver (PulpSolver): The solver to add the target for.

        Returns:
            LpElement: The sum of the two cell value_list.
        """
        lhs: LpElement = solver.cell_values[self.cell1.row][self.cell1.column]
        rhs: LpElement = solver.cell_values[self.cell2.row][self.cell2.column]
        return lhs + rhs

    def css(self) -> dict:
        """Get the CSS styles for the VariableSumPair.

        Returns:
            dict: A dictionary defining the CSS styles for the `VariableSumPair`.
            The `.FixedSumPair` style specifies the fill color as cyan, stroke
            width as 1, and stroke color as black.
        """
        return {
            '.FixedSumPair': {
                'fill': 'cyan',
                'stroke-width': 1,
                'stroke': 'black',
            },
        }
