"""TestLessThanEqualDifferencePair."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.items.less_than_equal_difference_pair import LessThanEqualDifferencePair
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_different_pair import TestDifferencePair


class TestLessThanEqualDifferencePair(TestDifferencePair):
    """Test suite for the LessThanEqualDifferencePair class, inheriting from TestDifferencePair."""

    def setUp(self) -> None:
        """Set up the test case, initializing the constraint and board for the LessThanEqualDifferencePair instance."""
        super().setUp()
        self.item = LessThanEqualDifferencePair(
            self.board,
            Cell.make(self.board, 1, 2),
            Cell.make(self.board, 1, 3),
            [1, 2]
        )
        self.size = 2

    @property
    def clazz(self):
        """Return the LessThanEqualDifferencePair class."""
        return LessThanEqualDifferencePair

    @property
    def config(self) -> str:
        """Return the configuration string for LessThanEqualDifferencePair."""
        return "LessThanEqualDifferencePair: 12-13=1,2"

    @property
    def has_rule(self) -> bool:
        """Return whether the LessThanEqualDifferencePair instance has start rule."""
        return False

    @property
    def difference(self) -> int:
        """Return the difference for the LessThanEqualDifferencePair instance."""
        return 0

    @property
    def representation(self) -> str:
        """Return the string representation of the LessThanEqualDifferencePair instance."""
        return (
            "LessThanEqualDifferencePair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3), "
            "[1, 2]"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the LessThanEqualDifferencePair instance should belong to."""
        return {Cell, ComposedItem, DifferencePair, Item, LessThanEqualDifferencePair, Pair, Region}

    def test_difference(self):
        """Test the difference property of the LessThanEqualDifferencePair instance."""
        self.assertEqual(self.difference, self.item.difference)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
