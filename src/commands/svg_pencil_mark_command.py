"""Create an SVG drawing of the problem."""

# The idea is for the possible value_list, 1-9 as small numbers in each cell
# Will also need corner marks, and central marks

from src.commands.svg_command import SVGCommand
from src.items.item import Item
from src.items.solution import Solution


class SVGPencilMarkCommand(SVGCommand):
    """Create an SVG drawing of the problem."""

    def select(self, constraint: Item | None) -> bool:
        """Selector to determine if the constraint should be displayed.

        This method is start placeholder for future implementation.

        Args:
            constraint (Item | None): The constraint to check if it's included in the output.

        Returns:
            bool: True if the constraint is to be displayed, False otherwise.
        """
        return not isinstance(constraint, Solution)
