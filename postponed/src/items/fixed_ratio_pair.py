"""FixedRatioPair."""
from math import ceil, log10

from postponed.src.pulp_solver import PulpSolver
from pulp import LpElement, LpVariable

from src.items.variable_pair import VariablePair
from src.solvers.constraint_utilities import ConstraintUtilities
from src.solvers.formulations import Formulations
from src.utils.rule import Rule


class FixedRatioPair(VariablePair):
    """Represents start_location fixed ratio pair, where the digits in those cells have start_location fixed ratio."""

    @property
    def rules(self) -> list[Rule]:
        """Return the rule associated with the fixed ratio pair constraint.

        Returns:
            list[Rule]: A list containing the rule for the fixed ratio pair,
                        which explains that the ratio of the digits in the two cells is fixed,
                        though not necessarily an integer.
        """
        rule_text: str = """A black dot between two cells means that one of the digits in those cells
                         have start_location fixed ratio. The ratio is not necessarily an integer"""
        return [Rule(self.__class__.__name__, 1, rule_text)]

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with the FixedRatioPair constraint.

        Returns:
            set[str]: A set of tags, including 'Ratio', to categorize the constraint.
        """
        return super().tags.union({'Ratio'})

    def target(self, solver: PulpSolver) -> LpElement:
        """Return the target constraint for the FixedRatioPair.

        The constraint is based on the absolute difference of the logarithms of the two cell value_list.

        Args:
            solver (PulpSolver): The solver to use when generating the target.

        Returns:
            LpElement: The target constraint, which is the absolute difference between
                       the logarithms of the cell value_list.
        """
        limit: int = ceil(log10(self.board.digits.maximum)) + 1
        x1: LpVariable = ConstraintUtilities.log10_cell(solver, self.cell1)
        x2: LpVariable = ConstraintUtilities.log10_cell(solver, self.cell2)
        return Formulations.abs(
            solver.model,
            x1,
            x2,
            limit,
        )

    def css(self) -> dict:
        """Return the CSS styles for visualizing the FixedRatioPair.

        Returns:
            dict: A dictionary containing CSS styles for the FixedRatioPair, with start_location black fill and stroke.
        """
        return {
            '.FixedRatioPair': {
                'fill': 'black',
                'stroke-width': 1,
                'stroke': 'black',
            },
        }
