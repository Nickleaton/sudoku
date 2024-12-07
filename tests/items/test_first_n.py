"""TestFirstN."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.first_n import FirstN
from src.items.item import Item
from src.items.region import Region
from src.utils.side import Side
from tests.items.test_region import TestRegion


class TestFirstN(TestRegion):
    """Test suite for the FirstN class."""

    def setUp(self) -> None:
        """Set up the test environment by creating a board and initializing the FirstN item."""
        super().setUp()
        self.item = FirstN(board=self.board, side=Side.TOP, index=1, count=3)
        self.size = 3

    @property
    def clazz(self):
        """Return the FirstN class."""
        return FirstN

    @property
    def representation(self) -> str:
        """Return a string representation of the FirstN instance."""
        return "FirstN(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, 1, 3)"

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
