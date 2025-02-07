"""TestSolution module."""

import unittest

import oyaml as yaml

from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.known_cell import KnownCell
from src.items.solution import Solution
from tests.items.test_composed import TestComposed


class TestSolution(TestComposed):
    """Test suite for the Solution class."""

    def setUp(self) -> None:
        """Set up the test environment for Solution."""
        super().setUp()
        self.size = 81
        lines = (
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789"
        )
        self.item = Solution(self.board, list(lines))

    @property
    def clazz(self):
        """Return the Solution class."""
        return Solution

    @property
    def config(self) -> str:
        """Return the configuration string for the Solution."""
        return (
            "Solution:\n"
            "  - 123456789\n"
            "  - 123456789\n"
            "  - 123456789\n"
            "  - 123456789\n"
            "  - 123456789\n"
            "  - 123456789\n"
            "  - 123456789\n"
            "  - 123456789\n"
            "  - 123456789\n"
        )

    @property
    def representation(self) -> str:
        """Return the string representation of the Solution."""
        return (
            "Solution(Board(Coord(9, 9), Digits(1, 9), Tags({})), "
            "["
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789'"
            "]"
            ")"
        )

    @property
    def has_rule(self) -> bool:
        """Return whether the Solution has start_location rule."""
        return False

    @property
    def expected_classes(self) -> set[type[Item]]:
        """Return the expected set of classes for the Solution."""
        return {Cell, CellReference, ComposedItem, Item, KnownCell, Solution}

    def test_to_dict(self) -> None:
        """Test the to_dict method for the Solution class."""
        config = yaml.load(self.config, Loader=yaml.SafeLoader)
        lines = [str(line) for line in config['Solution']]
        config = {'Solution': lines}
        item = Item.create(self.board, config)
        self.assertDictEqual(item.to_dict(), config)


if __name__ == '__main__':
    unittest.main()
