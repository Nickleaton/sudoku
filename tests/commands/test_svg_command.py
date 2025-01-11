"""TestSvgCommand."""
import unittest

from src.commands.svg_command import SVGCommand
from src.items.item import Item
from tests.commands.test_simple_command import TestSimpleCommand


class TestSVGCommand(TestSimpleCommand):
    """Test suite for the SVGCommand class."""

    def setUp(self) -> None:
        """Sets up the test environment for SVGCommand."""
        super().setUp()
        self.command = SVGCommand()
        self.representation = "SVGCommand()"

    def test_in_select(self):
        """Tests the `select` method for the `in_select` constraint.

        If the `in_select` property is not `None`, verifies that the
        `select` method of the command returns `True` for the constraint.
        """
        if (select := self.in_select) is not None:
            self.assertTrue(self.command.select(select))

    def test_out_select(self):
        """Tests the `select` method for the `out_select` constraint.

        If the `out_select` property is not `None`, verifies that the
        `select` method of the command returns `False` for the constraint.
        """
        if (select := self.out_select) is not None:
            self.assertFalse(self.command.select(select))

    @property
    def in_select(self) -> Item | None:
        """Gets a constraint that should be included in the output of the command.

        Returns:
            Item | None: An constraint that should be included in the output, or `None`.
        """
        return None

    @property
    def out_select(self) -> Item | None:
        """Gets a constraint that should not be included in the output of the command.

        Returns:
            Item | None: An constraint that should not be included in the output, or `None`.
        """
        return None


class TestSVGPencilMarkCommand(TestSVGCommand):
    """Test suite for SVGPencilMarkCommand class."""

    def setUp(self) -> None:
        """Set up the test environment for SVGPencilMarkCommand."""
        super().setUp()
        self.command = SVGPencilMarkCommand()
        self.representation = 'SVGPencilMarkCommand()'


class TestSVGSolutionCommand(TestSVGCommand):
    """Test suite for SVGSolutionCommand class."""

    def setUp(self):
        """Set up the test environment for SVGSolutionCommand."""
        super().setUp()
        self.command = SVGSolutionCommand()
        self.representation = 'SVGSolutionCommand()'

    @property
    def in_select(self):
        """Return a constraint to be included in the output of the command.

        If this property is not `None`, the `select` method of the command should
        return `True` for this constraint.

        Returns:
            Item: An constraint to be selected, or `None`.
        """
        return Solution(
            self.problem.board,
            [
                '123456789',
                '123456789',
                '123456789',
                '123456789',
                '123456789',
                '123456789',
                '123456789',
                '123456789',
                '123456789'
            ]
        )

    @property
    def out_select(self):
        """Return a constraint not to be included in the output of the command.

        If this property is not `None`, the `select` method of the command should
        return `False` for this constraint.

        Returns:
            Item: An constraint that should not be selected, or `None`.
        """
        return Battenburg(self.problem.board, Coord(2, 2))


class TestSVGProblemCommand(TestSVGCommand):
    """Test suite for SVGProblemCommand class."""

    def setUp(self) -> None:
        """Set up the test environment for SVGProblemCommand."""
        super().setUp()
        self.command = SVGProblemCommand()
        self.representation = 'SVGProblemCommand()'


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
