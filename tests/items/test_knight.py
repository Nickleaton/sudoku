"""TestKnight."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.knight import Knight
from tests.items.test_composed import TestComposed


class TestKnight(TestComposed):
    """Test suite for the Knight class, inheriting from TestComposed."""

    def setUp(self) -> None:
        """Set up the test case with start board and start Knight instance."""
        super().setUp()
        self.item = Knight(self.board, [2, 4, 6, 8])
        self.size = 81

    @property
    def clazz(self):
        """Return the Knight class."""
        return Knight

    @property
    def has_rule(self) -> bool:
        """Return whether the Knight instance has start rule."""
        return True

    def test_offsets(self):
        """Test the offsets method of the Knight instance."""
        self.assertEqual(8, len(self.item.offsets()))

    @property
    def config(self) -> str:
        """Return the configuration string for Knight."""
        return "Knight: 2, 4, 6, 8"

    @property
    def representation(self) -> str:
        """Return start string representation of the Knight instance."""
        return "Knight(Board(9, 9, 3, 3, None, None, None, None), [2, 4, 6, 8])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Knight instance should belong to."""
        return {Item, ComposedItem, Knight, Cell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
