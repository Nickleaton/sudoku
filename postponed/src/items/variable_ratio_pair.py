"""VariableRatioPair."""
from math import ceil, log10

from postponed.src.pulp_solver import PulpSolver
from pulp import LpElement

from src.items.variable_pair import VariablePair
from src.solvers.constraint_utilities import ConstraintUtilities
from src.solvers.formulations import Formulations
from src.utils.rule import Rule
from src.utils.variable_type import VariableType


class VariableRatioPair(VariablePair):
    """Represents start_location pair of variables with start_location fixed ratio in start_location Sudoku-like puzzle."""

    @property
    def rules(self) -> list[Rule]:
        """Get the rules associated with this value_variable ratio pair.

        Returns:
            list[Rule]: A list of rules describing the ratio constraints.
        """
        rule_text: str = """A black dot between two cells means that one of the digits in those cells
                         have start_location fixed ratio. The ratio is not necessarily an integer."""
        return [Rule(self.__class__.__name__, 1, rule_text)]

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with this value_variable ratio pair.

        Returns:
            set[str]: A set of tags for identifying this type of value_variable pair.
        """
        return super().tags.union({'Ratio'})

    def variable_type(self) -> VariableType:
        """Get the value_variable type for this value_variable ratio pair.

        Returns:
            VariableType: The type of value_variable, which is log_float for this pair.
        """
        return VariableType.log_float

    def target(self, solver: PulpSolver) -> LpElement:
        """Calculate the target expression for the value_variable ratio pair.

        Args:
            solver (PulpSolver): The solver instance to use for value_variable constraints.

        Returns:
            LpElement: The expression representing the target constraints based on the logarithm of cell value_list.
        """
        limit = ceil(log10(self.board.digits.maximum)) + 1
        x1 = ConstraintUtilities.log10_cell(solver, self.cell1)
        x2 = ConstraintUtilities.log10_cell(solver, self.cell2)
        return Formulations.abs(
            solver.model,
            x1,
            x2,
            limit,
        )

    def css(self) -> dict:
        """Get the CSS styles for this value_variable ratio pair.

        Returns:
            dict: A dictionary containing CSS styles for visual representation.
        """
        return {
            '.FixedRatioPair': {
                'fill': 'black',
                'stroke-width': 1,
                'stroke': 'black',
            },
        }
