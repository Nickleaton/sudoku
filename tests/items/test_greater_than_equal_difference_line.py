"""TestGreaterThanEqualDifferenceLine."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_line import DifferenceLine
from src.items.fixed_difference_pair import FixedDifferencePair
from src.items.fixed_pair import FixedPair
from src.items.greater_than_equal_difference_line import GreaterThanEqualDifferenceLine
from src.items.greater_than_equal_difference_pair import GreaterThanEqualDifferencePair
from src.items.item import Item
from src.items.line import Line
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_line import TestLine


class TestGreaterThanEqualDifferenceLine(TestLine):
    """Test suite for the GreaterThanEqualDifferenceLine class."""

    def setUp(self) -> None:
        """Set up the test case with a board and an instance of GreaterThanEqualDifferenceLine."""
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        cells = [Cell.make(self.board, 1, 1), Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3)]
        self.item = GreaterThanEqualDifferenceLine(self.board, cells, 9)
        self.size = 5

    @property
    def clazz(self):
        """Return the GreaterThanEqualDifferenceLine class."""
        return GreaterThanEqualDifferenceLine

    @property
    def config(self) -> str:
        """Return the configuration string for GreaterThanEqualDifferenceLine."""
        return "GreaterThanEqualDifferenceLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        """Return True to indicate the rule is present for GreaterThanEqualDifferenceLine."""
        return True

    @property
    def representation(self) -> str:
        """Return a string representation of the GreaterThanEqualDifferenceLine instance."""
        return (
            "GreaterThanEqualDifferenceLine"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "["
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 1), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            "]"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the GreaterThanEqualDifferenceLine should belong to."""
        return {Cell, ComposedItem, DifferenceLine, FixedDifferencePair, FixedPair, GreaterThanEqualDifferenceLine,
                GreaterThanEqualDifferencePair, Item, Line, Pair, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
