"""TestGermanWhisperLine."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_line import DifferenceLine
from src.items.fixed_difference_pair import FixedDifferencePair
from src.items.fixed_pair import FixedPair
from src.items.ge_difference_line import GEDifferenceLine
from src.items.ge_difference_pair import GEDifferencePair
from src.items.german_whisper_line import GermanWhisperLine
from src.items.item import Item
from src.items.line import Line
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_ge_difference_line import TestGEDifferenceLine


class TestGermanWhisperLine(TestGEDifferenceLine):
    """Test suite for the GermanWhisperLine class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        cells = [Cell.make(self.board, 1, 1), Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3)]
        self.item = GermanWhisperLine(self.board, cells)
        self.size = 5

    @property
    def clazz(self):
        """Return the GermanWhisperLine class."""
        return GermanWhisperLine

    @property
    def config(self) -> str:
        """Return the configuration string of the GermanWhisperLine."""
        return "GermanWhisperLine: 11, 12, 13"

    @property
    def representation(self) -> str:
        """Return the string representation of the GermanWhisperLine."""
        return (
            "GermanWhisperLine"
            "("
            "Board(9, 9, 3, 3, None), "
            "["
            "Cell(Board(9, 9, 3, 3, None), 1, 1), "
            "Cell(Board(9, 9, 3, 3, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None), 1, 3)"
            "]"
            ")"
        )

    @property
    def has_rule(self) -> bool:
        """Return whether the GermanWhisperLine has start rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the GermanWhisperLine should belong to."""
        return {Cell, ComposedItem, DifferenceLine, FixedDifferencePair, FixedPair, GermanWhisperLine,
                GEDifferenceLine, GEDifferencePair, Item, Line, Pair, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
