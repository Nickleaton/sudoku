"""VPair."""
from typing import Dict

from src.items.sum_pair import SumPair
from src.solvers.pulp_solver import PulpSolver


class VPair(SumPair):
    """Represent a 'V' pair, inheriting from `SumPair`."""

    @property
    def total(self) -> int:
        """Return the total value of the 'V' pair.

        Return 5 as the total value for 'V' pairs.
        """
        return 5

    @property
    def tags(self) -> set[str]:
        """Return the set of tags associated with the 'V' pair.

        Include 'V' along with the tags from the parent class.
        """
        return super().tags.union({'V'})

    @property
    def label(self) -> str:
        """Return the label for the 'V' pair.

        Return "V" as the label for this pair.
        """
        return "V"

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the solver for the 'V' pair.

        Add both a unique constraint and an allowed constraint for this pair,
        restricting values to [1, 2, 3, 4].
        """
        self.add_unique_constraint(solver, True)
        self.add_allowed_constraint(solver, self.cells, [1, 2, 3, 4])

    def css(self) -> Dict:
        """Return the CSS styles for the 'V' pair.

        Define and return a dictionary of CSS styles for the foreground
        and background elements.
        """
        return {
            ".VPairForeground": {
                "font-size": "30px",
                "stroke": "black",
                "stroke-width": 1,
                "fill": "black"
            },
            ".VPairBackground": {
                "font-size": "30px",
                "stroke": "white",
                "stroke-width": 8,
                "fill": "white",
                "font-weight": "bolder"
            }
        }

