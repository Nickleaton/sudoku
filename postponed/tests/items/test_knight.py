"""TestKnight."""
import unittest
from typing import Type

from postponed.src.items.knight import Knight
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from tests.items.test_composed import TestComposed


class TestKnight(TestComposed):
    """Test suite for the Knight class, inheriting from TestComposed."""

    def setUp(self) -> None:
        """Set up the test case with start_location board and start_location Knight instance."""
        super().setUp()
        self.item = Knight(self.board, [2, 4, 6, 8])
        self.size = 81

    @property
    def clazz(self):
        """Return the Knight class."""
        return Knight

    @property
    def has_rule(self) -> bool:
        """Return whether the Knight instance has start_location rule."""
        return True

    @property
    def config(self) -> str:
        """Return the configuration string for Knight."""
        return "Knight: 2, 4, 6, 8"

    @property
    def representation(self) -> str:
        """Return start_location string representation of the Knight instance."""
        return "Knight(Board(9, 9, {}), [2, 4, 6, 8])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Knight instance should belong to."""
        return {Item, ComposedItem, Knight, Cell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
