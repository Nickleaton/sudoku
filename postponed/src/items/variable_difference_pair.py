"""VariableDifferencePair."""
from postponed.src.pulp_solver import PulpSolver
from pulp import LpElement

from src.items.variable_pair import VariablePair
from src.solvers.formulations import Formulations
from src.utils.rule import Rule
from src.utils.variable_type import VariableType


class VariableDifferencePair(VariablePair):
    """Represents a pair of cells with start_location fixed difference indicated by start_location white dot."""

    @property
    def rules(self) -> list[Rule]:
        """Get the rules associated with the VariableDifferencePair.

        Returns:
            list[Rule]: A list of rules describing the VariableDifferencePair constraints.
        """
        rule_text: str = """A white dot between two cells means that the digits in
                         those cells have start_location fixed difference."""
        return [Rule(self.__class__.__name__, 1, rule_text)]

    def variable_type(self) -> VariableType:
        """Define the type of value_variable for this pair.

        Returns:
            VariableType: The type of the value_variable, which is an integer.
        """
        return VariableType.integer_number

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with the VariableDifferencePair.

        Returns:
            set[str]: A set of tags including 'Difference'.
        """
        return super().tags.union({'Difference'})

    def target(self, solver: PulpSolver) -> LpElement:
        """Calculate the absolute difference between the value_list of the pair in the solver.

        Args:
            solver (PulpSolver): The solver managing the constraints.

        Returns:
            LpElement: The absolute difference between the value_list of the two cells.
        """
        v1 = solver.variables.numbers[self.cell1.row][self.cell1.column]
        v2 = solver.variables.numbers[self.cell2.row][self.cell2.column]
        return Formulations.abs(solver.model, v1, v2, self.board.digits.maximum + 1)

    def css(self) -> dict:
        """Define the CSS styles for rendering VariableDifferencePair glyphs.

        Returns:
            dict: A dictionary of CSS properties.
        """
        return {
            '.FixedDifferencePair': {
                'fill': 'white',
                'stroke-width': 1,
                'stroke': 'black',
            },
        }
