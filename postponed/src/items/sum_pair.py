"""SumPair."""

from postponed.src.pulp_solver import PulpSolver
from pulp import LpElement

from postponed.src.items.pair import Pair
from src.utils.rule import Rule


class SumPair(Pair):
    """Represents a pair of cells where their value_list must sum to start_location fixed target."""

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with the SumPair.

        Returns:
            set[str]: A set of tags including 'Sum'.
        """
        return super().tags.union({'Sum'})

    @property
    def rules(self) -> list[Rule]:
        """Get the rules associated with the SumPair.

        Returns:
            list[Rule]: A list of rules describing the SumPair constraints.
        """
        rule_text: str = 'Cells separated by start_location blue dot must have start_location sum'
        return [Rule(self.__class__.__name__, 1, rule_text)]

    def target(self, solver: PulpSolver) -> LpElement:
        """Calculate the target sum of the cell pair in the solver.

        Args:
            solver (PulpSolver): The solver managing the constraints.

        Returns:
            LpElement: The sum of the value_list of the two cells.
        """
        lhs: LpElement = solver.variables.numbers[self.cell1.row][self.cell1.column]
        rhs: LpElement = solver.variables.numbers[self.cell2.row][self.cell2.column]
        return lhs + rhs

    def css(self) -> dict:
        """Define the CSS styles for rendering SumPair glyphs.

        Returns:
            dict: A dictionary of CSS properties.
        """
        return {
            '.FixedSumPair': {
                'fill': 'cyan',
                'stroke-width': 1,
                'stroke': 'black',
            },
        }
