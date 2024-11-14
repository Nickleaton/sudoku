"""Create an SVG drawing of the problem."""

from src.commands.svg_command import SVGCommand
from src.items.item import Item
from src.items.solution import Solution
from src.solvers.answer import Answer


class SVGProblemCommand(SVGCommand):
    """Create an SVG drawing of the problem."""

    def __init__(self, problem_field: str = "problem_svg"):
        """Initialize the SVGProblemCommand.

        Args:
            problem_field (str): The attribute of the problem that contains the root item to be drawn.
        """
        super().__init__(problem_field)

    def select(self, item: Item | None) -> bool:
        """Selector to determine if the item should be displayed.

        Args:
            item (Item | None): The item to check if it's included in the output.

        Returns:
            bool: True if the item is to be displayed, False otherwise.
        """
        return not isinstance(item, Solution) and not isinstance(item, Answer)
