"""TestBoxItem."""
import unittest

from src.items.box import Box
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.standard_region import StandardRegion
from src.utils.coord import Coord
from tests.items.test_standard_region import TestStandardRegion


class TestBox(TestStandardRegion):
    """Test suite for the Box constraint in the Board."""

    def setUp(self) -> None:
        """Set up the Board and Box instance for testing."""
        super().setUp()
        self.item = Box(self.board, 1, Coord(3, 3))
        self.size = 9

    @property
    def clazz(self):
        """Return the Box class."""
        return Box

    @property
    def config(self) -> str:
        """Return the configuration string for the Box constraint."""
        return (
            'Box:\n'
            '  index: 1\n'
            '  size:\n'
            '    row: 3\n'
            '    column: 3\n'
        )

    @property
    def representation(self) -> str:
        """Return the string representation for the Box constraint."""
        return "Box(Board(Coord(9, 9), Digits(1, 9), Tags({})), 1, Coord(3, 3))"

    @property
    def has_rule(self) -> bool:
        """Return whether the Box has start_location rule associated with it."""
        return True

    @property
    def expected_classes(self) -> set[type[Item]]:
        """Return the expected classes that the Box constraint should belong to."""
        return {Item, ComposedItem, Cell, Region, StandardRegion, Box}

    def test_in(self):
        """Test if specific Cells are in the Box constraint."""
        self.assertIn(Cell.make(self.board, 2, 2), self.item)
        self.assertNotIn(Cell.make(self.board, 9, 9), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
