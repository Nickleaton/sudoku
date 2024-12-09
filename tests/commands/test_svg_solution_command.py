"""TestSvgSolutionCommand."""
import unittest

from src.commands.svg_solution_command import SVGSolutionCommand
from src.items.battenburg import Battenburg
from src.items.item import Item
from src.items.solution import Solution
from src.utils.coord import Coord
from tests.commands.test_svg_command import TestSVGCommand


class TestSVGSolutionCommand(TestSVGCommand):
    """Test suite for SVGSolutionCommand class."""

    def setUp(self):
        """Set up the test environment for SVGSolutionCommand."""
        super().setUp()
        self.command = SVGSolutionCommand()
        self.representation = r"SVGSolutionCommand('board', 'constraints', 'svg')"

    @property
    def in_select(self):
        """Return an constraint to be included in the output of the command.

        If this property is not `None`, the `select` method of the command should
        return `True` for this constraint.

        Returns:
            Item: An constraint to be selected, or `None`.
        """
        return Solution(
            self.problem.board,
            [
                "123456789",
                "123456789",
                "123456789",
                "123456789",
                "123456789",
                "123456789",
                "123456789",
                "123456789",
                "123456789"
            ]
        )

    @property
    def out_select(self):
        """Return an constraint not to be included in the output of the command.

        If this property is not `None`, the `select` method of the command should
        return `False` for this constraint.

        Returns:
            Item: An constraint that should not be selected, or `None`.
        """
        return Battenburg(self.problem.board, Coord(2, 2))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
