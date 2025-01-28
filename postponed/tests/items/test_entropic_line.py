"""TestEntropicLine."""
import unittest
from typing import Type

from postponed.src.items.entropic_line import EntropicLine
from postponed.src.items.line import Line
from postponed.tests.items.test_line import TestLine
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestEntropicLine(TestLine):
    """Test suite for the EntropicLine class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        cells = [
            Cell.make(self.board, 1, 1),
            Cell.make(self.board, 1, 2),
            Cell.make(self.board, 1, 3),
            Cell.make(self.board, 1, 4),
            Cell.make(self.board, 1, 5),
            Cell.make(self.board, 1, 6)
        ]
        self.item = EntropicLine(self.board, cells)
        self.size = 6

    @property
    def config(self) -> str:
        """Return the configuration string for the EntropicLine."""
        return "EntropicLine: 11, 12, 13, 14, 15, 16"

    @property
    def clazz(self):
        """Return the EntropicLine class."""
        return EntropicLine

    @property
    def representation(self) -> str:
        """Return the string representation of the EntropicLine."""
        return (
            "EntropicLine"
            "("
            "Board(9, 9, {}), "
            "["
            "Cell(Board(9, 9, {}), 1, 1), "
            "Cell(Board(9, 9, {}), 1, 2), "
            "Cell(Board(9, 9, {}), 1, 3), "
            "Cell(Board(9, 9, {}), 1, 4), "
            "Cell(Board(9, 9, {}), 1, 5), "
            "Cell(Board(9, 9, {}), 1, 6)"
            "]"
            ")"
        )

    @property
    def has_rule(self) -> bool:
        """Return whether the EntropicLine has start_location rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the EntropicLine should belong to."""
        return {Cell, ComposedItem, EntropicLine, Item, Line, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
