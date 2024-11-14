"""Create an SVG drawing of the solution."""

from src.commands.svg_command import SVGCommand
from src.items.item import Item
from src.solvers.answer import Answer


class SVGAnswerCommand(SVGCommand):
    """Command to create an SVG drawing of the answer."""

    def select(self, item: Item | None) -> bool:
        """Determine if the item should be included in the output.

        Args:
            item (Item | None): The item to check for inclusion.

        Returns:
            bool: True if the item is to be displayed; otherwise, False.
        """
        return isinstance(item, Answer)
