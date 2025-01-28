"""TestMountainLine."""
import unittest
from typing import Type

from postponed.src.items.line import Line
from postponed.src.items.mountain_line import MountainLine
from postponed.tests.items.test_line import TestLine
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestMountain(TestLine):
    """Test suite for the MountainLine class."""

    def setUp(self) -> None:
        """Set up the test environment for MountainLine."""
        # Needs separate create from TestLine because of shape
        cells = [Cell.make(self.board, 2, 1), Cell.make(self.board, 1, 2), Cell.make(self.board, 2, 3)]
        self.item = self.clazz(self.board, cells)
        self.size = 3
        self.good_yaml = []
        self.bad_yaml = []

    @property
    def clazz(self):
        """Return the MountainLine class."""
        return MountainLine

    @property
    def config(self) -> str:
        """Return the configuration string for MountainLine."""
        return "MountainLine: 21, 12, 23"

    @property
    def representation(self) -> str:
        """Return the string representation of the MountainLine instance."""
        return (
            f"{self.clazz.__name__}(Board(9, 9, {{}}), "
            f"["
            f"Cell(Board(9, 9, {{}}), 2, 1), "
            f"Cell(Board(9, 9, {{}}), 1, 2), "
            f"Cell(Board(9, 9, {{}}), 2, 3)"
            f"]"
            f")"
        )

    @property
    def has_rule(self) -> bool:
        """Return whether the MountainLine instance has start_location rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the MountainLine instance should belong to."""
        return {Cell, ComposedItem, Item, Line, Region, MountainLine}

    def test_in(self):
        """Test if specific cells are in or not in the MountainLine instance."""
        self.assertIn(Cell.make(self.board, 1, 2), self.item)
        self.assertNotIn(Cell.make(self.board, 9, 9), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
