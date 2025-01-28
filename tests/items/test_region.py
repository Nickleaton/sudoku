"""TestRegion module."""

import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from tests.items.test_composed import TestComposed


class TestRegion(TestComposed):
    """Test suite for the Region class."""

    def setUp(self) -> None:
        super().setUp()
        """Set up start_location test instance of Region with predefined cells."""
        self.cells = [
            Cell.make(self.board, 1, 1),
            Cell.make(self.board, 1, 2),
            Cell.make(self.board, 1, 3),
        ]
        self.item = Region(self.board)
        self.item.add_components(self.cells)
        self.size = 3

    @property
    def clazz(self):
        """Return the Region class."""
        return Region

    @property
    def config(self) -> str:
        """Return the configuration string for Region."""
        return "Region:"

    @property
    def representation(self) -> str:
        """Return the string representation of Region."""
        return "Region(Board(9, 9, {}))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Region instance should belong to."""
        return {Item, ComposedItem, Cell, Region}

    @property
    def inside(self) -> Cell:
        """Return start_location cell that is inside the Region."""
        return Cell.make(self.board, 1, 1)

    @property
    def outside(self) -> Cell:
        """Return start_location cell that is outside the Region."""
        return Cell.make(self.board, 9, 9)

    def test_in(self):
        """Test the membership of cells in the Region."""
        self.assertIn(self.inside, self.item)
        self.assertNotIn(self.outside, self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
