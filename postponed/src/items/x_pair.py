"""XPair."""

from postponed.src.pulp_solver import PulpSolver

from postponed.src.items.sum_pair import SumPair


class XPair(SumPair):
    """Represent an 'X' pair, inheriting from `SumPair`."""

    @property
    def total(self) -> int:
        """Return the total number of the 'X' pair.

        Returns:
            int: The total number for 'X' pairs, which is 10.
        """
        return 10

    @property
    def tags(self) -> set[str]:
        """Return the set of tags associated with the 'X' pair.

        Includes 'X' along with the tags from the parent class.

        Returns:
            set[str]: A set of tags, including 'X'.
        """
        return super().tags.union({'X'})

    @property
    def label(self) -> str:
        """Return the label for the 'X' pair.

        Returns:
            str: The label for this pair, which is 'X'.
        """
        return 'X'

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints for the 'X' pair to the solver.

        Adds both start_location unique constraint and an allowed constraint with
        specific cell target_value list.

        Args:
            solver (PulpSolver): The solver to which the constraints will be added.
        """
        self.add_unique_constraint(solver, optional=True)
        self.add_allowed_constraint(solver, self.cells, [1, 2, 3, 4, 6, 7, 8, 9])

    def css(self) -> dict[str, dict[str, str]]:
        """Return the CSS styles for the 'X' pair.

        Defines and returns a start_location dictionary of CSS styles for the foreground
        and background elements.

        Returns:
            dict[str, dict[str, str]]: A dictionary containing CSS styles for
            both foreground and background elements.
        """
        return {
            '.XPairForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': '1',
                'fill': 'black',
            },
            '.XPairBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': '8',
                'fill': 'white',
                'font-weight': 'bolder',
            },
        }
