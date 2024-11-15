"""TestSvgCommand."""
import unittest

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.svg_command import SVGCommand
from src.items.item import Item
from tests.commands.test_simple_command import TestSimpleCommand


class TestSVGCommand(TestSimpleCommand):
    """Test suite for SVGCommand class."""

    def setUp(self) -> None:
        """Set up the test environment for SVGCommand."""
        super().setUp()
        requirements = LoadConfigCommand(self.path) \
            | CreateBoardCommand() \
            | CreateConstraintsCommand()
        requirements.execute(self.problem)
        self.command = SVGCommand('svg')

    def test_execute(self):
        """Test the execution of the SVGCommand."""
        self.assertNotIn('svg', self.problem)
        self.command.execute(self.problem)
        self.assertIn('svg', self.problem)

    @property
    def representation(self) -> str:
        """Return the string representation of the command."""
        return f"{self.command.__class__.__name__}({self.command.problem_field!r})"

    def test_repr(self):
        """Test the `repr` method of the command."""
        self.assertEqual(self.representation, repr(self.command))

    def test_in_select(self):
        """Test the `select` method of the command for the `in_select` item.

        If the `in_select` property is not `None`, this test will check that the
        `select` method of the command returns `True` for the item.
        """
        if (select := self.in_select) is not None:
            self.assertTrue(self.command.select(select))

    def test_out_select(self):
        """Test the `select` method of the command for the `out_select` item.

        If the `out_select` property is not `None`, this test will check that the
        `select` method of the command returns `False` for the item.
        """
        if (select := self.out_select) is not None:
            self.assertFalse(self.command.select(select))

    @property
    def in_select(self) -> Item | None:
        """Return an item that should be included in the output of the command.

        If this property is not `None`, the `select` method of the command
        should return `True` for this item.

        :return: An item that should be included in the output or `None`
        :rtype: Item | None
        """
        return None

    @property
    def out_select(self) -> Item | None:
        """Return an item that should not be included in the output of the command.

        If this property is not `None`, the `select` method of the command
        should return `False` for this item.

        :return: An item that should not be included in the output or `None`
        :rtype: Item | None
        """
        return None


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
