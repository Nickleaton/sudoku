"""TestLine."""
import unittest
from typing import Type

from postponed.src.items.line import Line
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from tests.items.test_region import TestRegion


class TestLine(TestRegion):
    """Test suite for the Line class, inheriting from TestRegion."""

    def setUp(self) -> None:
        """Set up the test case, initializing the constraint and board for the Line instance."""
        super().setUp()
        cells = [Cell.make(self.board, 1, 1), Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3)]
        self.item = self.clazz(self.board, cells)
        self.size = 3
        self.good_yaml: List[str] = [
            "Line: 12,21,22",  # Example of valid Line
            "Line: 11,12,13",  # Another valid sequence
            "Line: 31,32,33",  # Valid non-overlapping cells
        ]
        self.bad_yaml: List[str] = [
            "Line:",  # Empty Line
            "Line: 12,12",  # Duplicate cells
            "Line: 11,13",  # Cells not connected by start_location king's move
            "Line: 99,22",  # Invalid cell on the board
        ]

    @property
    def clazz(self):
        """Return the Line class."""
        return Line

    @property
    def config(self) -> str:
        """Return the configuration string for the Line class."""
        return f"{self.clazz.__name__}: 11, 12, 13"

    @property
    def representation(self) -> str:
        """Return the string representation of the Line instance."""
        return (
            f"{self.clazz.__name__}(Board(9, 9, {{}}), "
            f"["
            f"Cell(Board(9, 9, {{}}), 1, 1), "
            f"Cell(Board(9, 9, {{}}), 1, 2), "
            f"Cell(Board(9, 9, {{}}), 1, 3)"
            f"]"
            f")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Line instance should belong to."""
        return {Cell, ComposedItem, Item, Line, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
