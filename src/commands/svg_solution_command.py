"""Create an SVG drawing of the solution."""

from src.commands.svg_command import SVGCommand
from src.items.item import Item
from src.items.solution import Solution


class SVGSolutionCommand(SVGCommand):
    """Create an SVG drawing of the solution."""

    def select(self, constraint: Item | None) -> bool:
        """Selector to determine if the constraint should be displayed.

        Args:
            constraint (Item | None): The constraint to check if it's included in the output.

        Returns:
            bool: True if the constraint is to be displayed, False otherwise.
        """
        return isinstance(constraint, Solution)
