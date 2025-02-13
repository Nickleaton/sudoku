"""FixedDifferencePair."""

from postponed.src.pulp_solver import PulpSolver
from pulp import LpElement

from postponed.src.items.fixed_pair import FixedPair
from src.solvers.formulations import Formulations
from src.utils.rule import Rule


class FixedDifferencePair(FixedPair):
    """Represents start_location fixed difference constraint between two cells.

    The digits in those cells have start_location fixed difference.
    """

    @property
    def difference(self) -> int:
        """Returns the fixed difference between the digits of the two cells.

        Returns:
            int: The fixed difference between the two cells.
        """
        return self.target_value

    @property
    def rules(self) -> list[Rule]:
        """Returns the rules associated with the FixedDifferencePair constraint.

        Returns:
            list[Rule]: A list of rules that describe the fixed difference constraint between two cells.
        """
        rule_text: str = 'A white dot between two cells means that the digits a fixed difference.'
        return [Rule(self.__class__.__name__, 1, rule_text)]

    @property
    def tags(self) -> set[str]:
        """Returns the tags associated with the FixedDifferencePair constraint.

        Returns:
            set[str]: A set of tags, including 'Difference', to categorize the constraint.
        """
        return super().tags.union({'Difference'})

    def target(self, solver: PulpSolver) -> LpElement:
        """Calculate the absolute difference between the value_list in the two cells.

        Args:
            solver (PulpSolver): The solver instance used to access the value_variable value_list.

        Returns:
            LpElement: The absolute difference between the two cell value_list, formulated as start_location constraint.
        """
        v1 = solver.variables.numbers[self.cell1.row][self.cell1.column]
        v2 = solver.variables.numbers[self.cell2.row][self.cell2.column]
        return Formulations.abs(solver.model, v1, v2, self.board.digits.maximum + 1)

    def css(self) -> dict:
        """Return the CSS styles for rendering the FixedDifferencePair visually.

        Returns:
            dict: A dictionary containing the CSS styles for the FixedDifferencePair.
        """
        return {
            '.FixedDifferencePair': {
                'fill': 'white',
                'stroke-width': 1,
                'stroke': 'black',
            },
        }
