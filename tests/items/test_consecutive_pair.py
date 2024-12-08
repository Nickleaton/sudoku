"""TestConsecutivePair."""
import unittest
from typing import Optional, Type

from src.board.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.consecutive_pair import ConsecutivePair
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.items.less_than_equal_difference_pair import LessThanEqualDifferencePair
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_different_pair import TestDifferencePair


class TestConsecutivePair(TestDifferencePair):
    """Test suite for the ConsecutivePair class."""

    def setUp(self) -> None:
        """Set up the Board and ConsecutivePair instance for testing."""
        super().setUp()

        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = ConsecutivePair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3))
        self.size = 2

    @property
    def clazz(self):
        """Return the ConsecutivePair class."""
        return ConsecutivePair

    @property
    def config(self) -> str:
        """Return the configuration string for the ConsecutivePair."""
        return "ConsecutivePair: 12-13"

    @property
    def has_rule(self) -> bool:
        """Indicates if the ConsecutivePair has a rule."""
        return True

    @property
    def representation(self) -> str:
        """Return the string representation for the ConsecutivePair."""
        return (
            "ConsecutivePair("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            ")"
        )

    @property
    def difference(self) -> Optional[int]:
        """Return the difference between the two cells in the ConsecutivePair."""
        return 1

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the ConsecutivePair should belong to."""
        return {Cell, ComposedItem, ConsecutivePair, DifferencePair, Item, LessThanEqualDifferencePair, Pair, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
