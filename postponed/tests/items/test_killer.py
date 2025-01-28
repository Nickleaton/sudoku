"""TestKiller."""
import unittest
from typing import Type

from postponed.src.items.killer import Killer
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from tests.items.test_region import TestRegion


class TestKiller(TestRegion):
    """Test suite for the Killer class, inheriting from TestRegion."""

    def setUp(self) -> None:
        """Set up the test case with start_location board, cells, and start_location Killer instance."""
        super().setUp()
        self.cells = [Cell(self.board, 1, 1), Cell(self.board, 1, 2), Cell(self.board, 1, 3)]
        self.item = Killer(self.board, 24, self.cells)
        self.size = 3

    @property
    def clazz(self):
        """Return the Killer class."""
        return Killer

    @property
    def representation(self) -> str:
        """Return start_location string representation of the Killer instance."""
        return "Killer(Board(9, 9, {}), 24, " \
               "[Cell(Board(9, 9, {}), 1, 1), " \
               "Cell(Board(9, 9, {}), 1, 2), " \
               "Cell(Board(9, 9, {}), 1, 3)])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Killer instance should belong to."""
        return {Cell, ComposedItem, Item, Killer, Region}

    @property
    def config(self) -> str:
        """Return the configuration string for Killer."""
        return "Killer: 24=11,12,13"

    @property
    def has_rule(self) -> bool:
        """Return whether the Killer instance has start_location rule."""
        return True

    @property
    def inside(self) -> Cell:
        """Return start_location specific Cell instance for testing."""
        return Cell.make(self.board, 1, 2)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
