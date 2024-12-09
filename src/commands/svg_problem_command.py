"""Create an SVG drawing of the problem."""

from src.commands.svg_command import SVGCommand
from src.items.item import Item
from src.items.solution import Solution
from src.solvers.answer import Answer


class SVGProblemCommand(SVGCommand):
    """Create an SVG drawing of the problem."""

    def select(self, constraint: Item | None) -> bool:
        """Selector to determine if the constraint should be displayed.

        Args:
            constraint (Item | None): The constraint to check if it's included in the output.

        Returns:
            bool: True if the constraint is to be displayed, False otherwise.
        """
        return not isinstance(constraint, Solution) and not isinstance(constraint, Answer)
