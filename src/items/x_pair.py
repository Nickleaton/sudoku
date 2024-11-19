"""XPair."""


from src.items.sum_pair import SumPair
from src.solvers.pulp_solver import PulpSolver


class XPair(SumPair):
    """Represent an 'X' pair, inheriting from `SumPair`."""

    @property
    def total(self) -> int:
        """Return the total value of the 'X' pair.

        Return 10 as the total value for 'X' pairs.
        """
        return 10

    @property
    def tags(self) -> set[str]:
        """Return the set of tags associated with the 'X' pair.

        Include 'X' along with the tags from the parent class.
        """
        return super().tags.union({'X'})

    @property
    def label(self) -> str:
        """Return the label for the 'X' pair.

        Return "X" as the label for this pair.
        """
        return "X"

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints for the 'X' pair to the solver.

        Add both a unique constraint and an allowed constraint with specific cell values.
        """
        self.add_unique_constraint(solver, True)
        self.add_allowed_constraint(solver, self.cells, [1, 2, 3, 4, 6, 7, 8, 9])

    def css(self) -> dict:
        """Return the CSS styles for the 'X' pair.

        Define and return a dictionary of CSS styles for the foreground
        and background elements.
        """
        return {
            ".XPairForeground": {
                "font-size": "30px",
                "stroke": "black",
                "stroke-width": 1,
                "fill": "black"
            },
            ".XPairBackground": {
                "font-size": "30px",
                "stroke": "white",
                "stroke-width": 8,
                "fill": "white",
                "font-weight": "bolder"
            }
        }
