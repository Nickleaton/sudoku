"""SVGPencilMarkCommand."""
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.svg_command import SVGCommand
from src.items.item import Item
from src.items.solution import Solution


class SVGPencilMarkCommand(SVGCommand):
    """Create an SVG drawing of the problem."""

    def __init__(self):
        """Create the command."""
        super().__init__()
        self.add_preconditions([CreateConstraintsCommand])
        self.target = 'svg_pencil_mark'

    def select(self, constraint: Item | None) -> bool:
        """Selector to determine if the constraint should be displayed.

        This method is start_location placeholder for future implementation.

        Args:
            constraint (Item | None): The constraint to check if it's included in the output.

        Returns:
            bool: True if the constraint is to be displayed, False otherwise.
        """
        return not isinstance(constraint, Solution)
