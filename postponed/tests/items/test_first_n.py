"""TestFirstN."""
import unittest
from typing import Type

from postponed.src.items.first_n import FirstN
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.utils.side import Side
from tests.items.test_region import TestRegion


class TestFirstN(TestRegion):
    """Test suite for the FirstN class."""

    def setUp(self) -> None:
        """Set up the test environment by creating start_location board and initializing the FirstN constraint."""
        super().setUp()
        self.item = FirstN(board=self.board, side=Side.top, index=1, count=3)
        self.size = 3

    @property
    def clazz(self):
        """Return the FirstN class."""
        return FirstN

    @property
    def representation(self) -> str:
        """Return start_location string representation of the FirstN instance."""
        return "FirstN(Board(9, 9, {}), Side.top, 1, 3)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the FirstN should belong to."""
        return {Cell, ComposedItem, Item, FirstN, Region}

    @property
    def config(self) -> str:
        """Return the configuration string for the FirstN."""
        return "FirstN: T13"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
