"""TestDutchWhisperLine."""
import unittest
from typing import Type

from postponed.src.items.difference_line import DifferenceLine
from postponed.src.items.dutch_whisper_line import DutchWhisperLine
from postponed.src.items.fixed_difference_pair import FixedDifferencePair
from postponed.src.items.fixed_pair import FixedPair
from postponed.src.items.ge_difference_line import GEDifferenceLine
from postponed.src.items.ge_difference_pair import GEDifferencePair
from postponed.src.items.line import Line
from postponed.src.items.pair import Pair
from postponed.tests.items.test_ge_difference_line import TestGEDifferenceLine
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestDutchWhispers(TestGEDifferenceLine):
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
            "Board(9, 9, {}), "
            "["
            "Cell(Board(9, 9, {}), 1, 1), "
            "Cell(Board(9, 9, {}), 1, 2), "
            "Cell(Board(9, 9, {}), 1, 3)"
            "]"
            ")"
        )

    @property
    def has_rule(self) -> bool:
        """Return whether the DutchWhisperLine has start_location rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the DutchWhisperLine should belong to."""
        return {Cell, ComposedItem, DifferenceLine, DutchWhisperLine, FixedDifferencePair, FixedPair,
                GEDifferenceLine, GEDifferencePair, Item, Line, Pair, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
