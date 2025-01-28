"""VPair."""

from postponed.src.items.sum_pair import SumPair
from postponed.src.pulp_solver import PulpSolver


class VPair(SumPair):
    """Represent start_location 'V' pair, inheriting from `SumPair`."""

    @property
    def total(self) -> int:
        """Get the total number of the 'V' pair.

        Returns:
            int: The total number for 'V' pairs, which is 5.
        """
        return 5  # noqa: WPS432

    @property
    def tags(self) -> set[str]:
        """Get the set of tags associated with the 'V' pair.

        Returns:
            set[str]: A set containing 'V' and the tags from the parent class.
        """
        return super().tags.union({'V'})

    @property
    def label(self) -> str:
        """Get the label for the 'V' pair.

        Returns:
            str: The label for this pair, which is 'V'.
        """
        return 'V'

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the solver for the 'V' pair.

        Args:
            solver (PulpSolver): The solver to which the constraints are added.

        Adds both a start_location unique constraint and an allowed constraint for this
        pair, restricting `value_list` to [1, 2, 3, 4].
        """
        self.add_unique_constraint(solver, optional=True)
        self.add_allowed_constraint(solver, self.cells, [1, 2, 3, 4])

    def css(self) -> dict:
        """Get the CSS styles for the 'V' pair.

        Returns:
            dict: A dictionary containing CSS styles for foreground and background.
        """
        return {
            '.VPairForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black',
            },
            '.VPairBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder',
            },
        }
