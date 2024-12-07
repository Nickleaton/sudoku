"""TestFixedDifferencePair."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.fixed_difference_pair import FixedDifferencePair
from src.items.fixed_pair import FixedPair
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_fixed_pair import TestFixedPair


class TestFixedDifferencePair(TestFixedPair):
    """Test suite for the FixedDifferencePair class."""

    def setUp(self) -> None:
        """Set up the test environment by creating a board and initializing the FixedDifferencePair item."""
        super().setUp()
        self.item = FixedDifferencePair(
            self.board,
            Cell.make(self.board, 1, 2),
            Cell.make(self.board, 1, 3),
            1
        )
        self.size = 2

    @property
    def clazz(self):
        """Return the FixedDifferencePair class."""
        return FixedDifferencePair

    @property
    def representation(self) -> str:
        """Return a string representation of the FixedDifferencePair instance."""
        return (
            "FixedDifferencePair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3), "
            "1"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the FixedDifferencePair."""
        return "FixedDifferencePair: 12-13=1"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the FixedDifferencePair should belong to."""
        return {Cell, Item, Pair, FixedPair, FixedDifferencePair, ComposedItem, Region}

    @property
    def has_rule(self) -> bool:
        """Return True if the FixedDifferencePair has a rule, otherwise False."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
