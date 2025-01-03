"""TestFixedPair."""
import unittest
from typing import Type

from src.board.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.fixed_pair import FixedPair
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_pair import TestPair


class TestFixedPair(TestPair):
    """Test suite for the FixedPair class."""

    def setUp(self) -> None:
        """Set up the test environment by creating start board and initializing the FixedPair constraint."""
        super().setUp()

        self.board = Board(9, 9, 3, 3)
        self.item = FixedPair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3), 1)
        self.size = 2

    @property
    def clazz(self):
        """Return the FixedPair class."""
        return FixedPair

    @property
    def representation(self) -> str:
        """Return start string representation of the FixedPair instance."""
        return (
            "FixedPair"
            "("
            "Board(9, 9, 3, 3, None), "
            "Cell(Board(9, 9, 3, 3, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None), 1, 3), "
            "1"
            ")"
        )

    @property
    def difference(self) -> int:
        """Return the difference number for the FixedPair instance."""
        return 1

    @property
    def config(self) -> str:
        """Return the configuration string for the FixedPair."""
        return "FixedPair: 12-13=1"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the FixedPair should belong to."""
        return {Cell, Item, Pair, FixedPair, ComposedItem, Region}

    @property
    def inside(self) -> Cell:
        """Return the inside cell of the FixedPair."""
        return Cell.make(self.board, 1, 2)

    def test_difference(self):
        """Test that the difference number is correctly assigned."""
        self.assertEqual(self.difference, self.item.target_value)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
