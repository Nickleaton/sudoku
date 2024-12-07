"""TestDutchWhisperLine."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_line import DifferenceLine
from src.items.dutch_whisper_line import DutchWhisperLine
from src.items.fixed_difference_pair import FixedDifferencePair
from src.items.fixed_pair import FixedPair
from src.items.greater_than_equal_difference_line import GreaterThanEqualDifferenceLine
from src.items.greater_than_equal_difference_pair import GreaterThanEqualDifferencePair
from src.items.item import Item
from src.items.line import Line
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_greater_than_equal_difference_line import TestGreaterThanEqualDifferenceLine


class TestDutchWhispers(TestGreaterThanEqualDifferenceLine):
    """Test suite for the DutchWhisperLine class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        cells = [Cell.make(self.board, 1, 1), Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3)]
        self.item = DutchWhisperLine(self.board, cells)
        self.size = 5

    @property
    def clazz(self):
        """Return the DutchWhisperLine class."""
        return DutchWhisperLine

    @property
    def config(self) -> str:
        """Return the configuration string for the DutchWhisperLine."""
        return "DutchWhisperLine: 11, 12, 13"

    @property
    def representation(self) -> str:
        """Return the string representation of the DutchWhisperLine."""
        return (
            "DutchWhisperLine"
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
    def has_rule(self) -> bool:
        """Return whether the DutchWhisperLine has a rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the DutchWhisperLine should belong to."""
        return {Cell, ComposedItem, DifferenceLine, DutchWhisperLine, FixedDifferencePair, FixedPair,
                GreaterThanEqualDifferenceLine, GreaterThanEqualDifferencePair, Item, Line, Pair, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
