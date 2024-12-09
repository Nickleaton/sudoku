"""TestGreaterThanEqualDifferencePair."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.fixed_difference_pair import FixedDifferencePair
from src.items.fixed_pair import FixedPair
from src.items.greater_than_equal_difference_pair import GreaterThanEqualDifferencePair
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_different_pair import TestDifferencePair


class TestGreaterThanEqualDifferencePair(TestDifferencePair):
    """Test suite for the GreaterThanEqualDifferencePair class."""

    def setUp(self) -> None:
        """Set up the test case with start board and an instance of GreaterThanEqualDifferencePair."""
        super().setUp()
        self.item = GreaterThanEqualDifferencePair(
            self.board,
            Cell.make(self.board, 1, 2),
            Cell.make(self.board, 1, 3),
            1
        )
        self.size = 2

    @property
    def clazz(self):
        """Return the GreaterThanEqualDifferencePair class."""
        return GreaterThanEqualDifferencePair

    @property
    def config(self) -> str:
        """Return the configuration string for GreaterThanEqualDifferencePair."""
        return "GreaterThanEqualDifferencePair: 12-13=1"

    @property
    def has_rule(self) -> bool:
        """Return True to indicate the rule is present for GreaterThanEqualDifferencePair."""
        return True

    @property
    def difference(self) -> int:
        """Return the difference number for the GreaterThanEqualDifferencePair."""
        return 1

    @property
    def representation(self) -> str:
        """Return start string representation of the GreaterThanEqualDifferencePair instance."""
        return (
            "GreaterThanEqualDifferencePair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3), "
            "1"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the GreaterThanEqualDifferencePair should belong to."""
        return {Cell, FixedDifferencePair, FixedPair, Item, Pair, GreaterThanEqualDifferencePair, ComposedItem, Region}

    def test_difference(self):
        """Test that the difference is correctly calculated."""
        self.assertEqual(self.difference, self.item.difference)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
