"""TestOutside."""
import unittest
from typing import Type

from postponed.src.items.first_n import FirstN
from postponed.src.items.outside import Outside
from postponed.tests.items.test_first_n import TestFirstN
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.utils.side import Side


class TestOutside(TestFirstN):
    """Test suite for the Outside class."""

    def setUp(self) -> None:
        """Set up the test environment for Outside."""
        super().setUp()
        self.item = Outside(self.board, Side.top, 1, [1, 2, 3])
        self.size = 3

    @property
    def clazz(self):
        """Return the Outside class."""
        return Outside

    @property
    def representation(self) -> str:
        """Return the string representation of the Outside instance."""
        return "Outside(Board(9, 9, {}), Side.top, 1, [1, 2, 3])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Outside instance should belong to."""
        return {Cell, ComposedItem, FirstN, Item, Outside, Region}

    @property
    def config(self) -> str:
        """Return the configuration string for Outside."""
        return "Outside: T1=123"

    @property
    def has_rule(self) -> bool:
        """Return whether the Outside instance has start_location rule."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
