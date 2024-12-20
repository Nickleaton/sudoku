"""Create an SVG drawing of the problem."""

# The idea is for the possible values, 1-9 as small numbers in each cell
# Will also need corner marks, and central marks

from src.commands.svg_command import SVGCommand
from src.items.item import Item
from src.items.solution import Solution


class SVGPencilMarkCommand(SVGCommand):
    """Create an SVG drawing of the problem."""

    def select(self, item: Item | None) -> bool:
        """Selector to determine if the item should be displayed.

        This method is a placeholder for future implementation.

        Args:
            item (Item | None): The item to check if it's included in the output.

        Returns:
            bool: True if the item is to be displayed, False otherwise.
        """
        return not isinstance(item, Solution)
