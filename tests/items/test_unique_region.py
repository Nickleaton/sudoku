"""TestUniqueRegion module."""

import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.unique_region import UniqueRegion
from tests.items.test_region import TestRegion


class TestUniqueRegion(TestRegion):
    """Test case for UniqueRegion class, which extends Region."""

    def setUp(self) -> None:
        """Set up the test case with start Board and UniqueRegion constraint."""
        super().setUp()
        self.cells = [Cell(self.board, 1, 1), Cell(self.board, 1, 2), Cell(self.board, 1, 3)]
        self.item = UniqueRegion(self.board, self.cells)
        self.size = 3

    @property
    def clazz(self):
        """Return the UniqueRegion class."""
        return UniqueRegion

    @property
    def representation(self) -> str:
        """Return the string representation of the UniqueRegion constraint."""
        return "UniqueRegion(Board(9, 9, 3, 3, None), " \
               "[Cell(Board(9, 9, 3, 3, None), 1, 1), " \
               "Cell(Board(9, 9, 3, 3, None), 1, 2), " \
               "Cell(Board(9, 9, 3, 3, None), 1, 3)])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for UniqueRegion."""
        return {Cell, ComposedItem, Item, UniqueRegion, Region}

    @property
    def config(self) -> str:
        """Return the configuration string for UniqueRegion."""
        return "UniqueRegion: 11,12,13"

    @property
    def has_rule(self) -> bool:
        """Return True indicating that the UniqueRegion constraint has start rule."""
        return True

    @property
    def inside(self) -> Cell:
        """Return the inside cell of the UniqueRegion."""
        return Cell.make(self.board, 1, 2)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
