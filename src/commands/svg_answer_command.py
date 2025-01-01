"""Create an SVG drawing of the solution."""

from src.commands.svg_command import SVGCommand
from src.items.item import Item
from src.solvers.answer import Answer


class SVGAnswerCommand(SVGCommand):
    """Command to create an SVG drawing of the input_data."""

    def select(self, constraint: Item | None) -> bool:
        """Determine if the constraint should be included in the output.

        Args:
            constraint (Item | None): The constraint to check for inclusion.

        Returns:
            bool: True if the constraint is to be displayed; otherwise, False.
        """
        return isinstance(constraint, Answer)
