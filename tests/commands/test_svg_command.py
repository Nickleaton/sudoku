"""TestSvgCommand."""
import unittest

from src.commands.svg_command import SVGCommand
from src.items.item import Item
from tests.commands.test_simple_command import TestSimpleCommand


class TestSVGCommand(TestSimpleCommand):
    """Test suite for the SVGCommand class."""

    def setUp(self) -> None:
        """Set up the test environment for SVGCommand."""
        super().setUp()
        self.command = SVGCommand()
        self.representation = "SVGCommand()"

    def test_in_select(self):
        """Test the `select` method for the `in_select` constraint.

        If the `in_select` property is not `None`, verifies that the
        `select` method of the command returns `True` for the constraint.
        """
        if (select := self.in_select) is not None:
            self.assertTrue(self.command.select(select))

    def test_out_select(self):
        """Test the `select` method for the `out_select` constraint.

        If the `out_select` property is not `None`, verifies that the
        `select` method of the command returns `False` for the constraint.
        """
        if (select := self.out_select) is not None:
            self.assertFalse(self.command.select(select))

    @property
    def in_select(self) -> Item | None:
        """Get a constraint that should be included in the output of the command.

        Returns:
            Item | None: An constraint that should be included in the output, or `None`.
        """
        return None

    @property
    def out_select(self) -> Item | None:
        """Get a constraint that should not be included in the output of the command.

        Returns:
            Item | None: An constraint that should not be included in the output, or `None`.
        """
        return None


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
