"""SumPair."""

from pulp import LpElement

from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class SumPair(Pair):
    """Represents start pair of cells where their value_list must sum to start fixed target."""

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
        return [
            Rule(
                self.__class__.__name__,
                1,
                "Cells separated by start blue dot must have start sum"
            )
        ]

    def target(self, solver: PulpSolver) -> LpElement:
        """Calculate the target sum of the cell pair in the solver.

        Args:
            solver (PulpSolver): The solver managing the constraints.

        Returns:
            LpElement: The sum of the value_list of the two cells.
        """
        return solver.values[self.cell_1.row][self.cell_1.column] + solver.values[self.cell_2.row][self.cell_2.column]

    def css(self) -> dict:
        """Define the CSS styles for rendering SumPair glyphs.

        Returns:
            dict: A dictionary of CSS properties.
        """
        return {
            '.FixedSumPair': {
                'fill': 'cyan',
                'stroke-width': 1,
                'stroke': 'black'
            }
        }
