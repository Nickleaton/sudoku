"""TestPair."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_region import TestRegion


class TestPair(TestRegion):
    """Test suite for the Pair class."""

    def setUp(self) -> None:
        """Set up the test environment for Pair."""
        super().setUp()
        self.item = Pair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3))
        self.size = 2

    @property
    def clazz(self):
        """Return the Pair class."""
        return Pair

    @property
    def representation(self) -> str:
        """Return the string representation of the Pair instance."""
        return (
            "Pair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for Pair."""
        return "Pair: 12-13"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Pair instance should belong to."""
        return {Cell, Item, Pair, ComposedItem, Region}

    @property
    def inside(self) -> Cell:
        """Return the first Cell in the Pair."""
        return Cell.make(self.board, 1, 2)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
