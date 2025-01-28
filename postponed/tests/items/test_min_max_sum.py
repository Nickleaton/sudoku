"""TestMinMaxSum."""
import unittest
from typing import Type

from postponed.src.items.first_n import FirstN
from postponed.src.items.min_max_sum import MinMaxSum
from postponed.tests.items.test_first_n import TestFirstN
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.utils.side import Side


class TestMinMaxSum(TestFirstN):
    """Test suite for the MinMaxSum class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.item = MinMaxSum(self.board, Side.top, 1, 20)
        self.size = 3

    @property
    def clazz(self):
        """Return the MinMaxSum class."""
        return MinMaxSum

    @property
    def representation(self) -> str:
        """Return the string representation of the MinMaxSum instance."""
        return "MinMaxSum(Board(9, 9, {}), Side.top, 20)"

    @property
    def config(self) -> str:
        """Return the configuration string for the MinMaxSum instance."""
        return "MinMaxSum: T1=20"

    @property
    def has_rule(self) -> bool:
        """Return whether the MinMaxSum instance has start_location rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the MinMaxSum instance should belong to."""
        return {Cell, ComposedItem, FirstN, MinMaxSum, Item, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
