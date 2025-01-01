"""TestGEDifferenceLine."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_line import DifferenceLine
from src.items.fixed_difference_pair import FixedDifferencePair
from src.items.fixed_pair import FixedPair
from src.items.ge_difference_line import GEDifferenceLine
from src.items.ge_difference_pair import GEDifferencePair
from src.items.item import Item
from src.items.line import Line
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_line import TestLine


class TestGEDifferenceLine(TestLine):
    """Test suite for the GEDifferenceLine class."""

    def setUp(self) -> None:
        """Set up the test case with start board and an instance of GEDifferenceLine."""
        super().setUp()
        cells = [Cell.make(self.board, 1, 1), Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3)]
        self.item = GEDifferenceLine(self.board, cells, 5)
        self.size = 5

    @property
    def clazz(self):
        """Return the GEDifferenceLine class."""
        return GEDifferenceLine

    @property
    def config(self) -> str:
        """Return the configuration string for GEDifferenceLine."""
        return "GEDifferenceLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        """Return True to indicate the rule is present for GEDifferenceLine."""
        return True

    @property
    def representation(self) -> str:
        """Return start string representation of the GEDifferenceLine instance."""
        return (
            "GEDifferenceLine"
            "("
            "Board(9, 9, 3, 3, None), "
            "["
            "Cell(Board(9, 9, 3, 3, None), 1, 1), "
            "Cell(Board(9, 9, 3, 3, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None), 1, 3)"
            "], "
            "5"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the GEDifferenceLine should belong to."""
        return {Cell, ComposedItem, DifferenceLine, FixedDifferencePair, FixedPair, GEDifferenceLine,
                GEDifferencePair, Item, Line, Pair, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
