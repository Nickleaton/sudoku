"""TestStandardRegion module."""

import unittest

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.standard_region import StandardRegion
from tests.items.test_region import TestRegion


class TestStandardRegion(TestRegion):
    """Test suite for the StandardRegion class."""

    def setUp(self) -> None:
        """Set up the test environment for StandardRegion."""
        super().setUp()
        self.item = StandardRegion(self.board, 1)
        self.size = 0

    @property
    def clazz(self):
        """Return the StandardRegion class."""
        return StandardRegion

    @property
    def config(self) -> str:
        """Return the configuration string for StandardRegion."""
        return f"{self.clazz.__name__}: 1"

    @property
    def representation(self) -> str:
        """Return the string representation of StandardRegion."""
        return "StandardRegion(Board(Coord(9, 9), Digits(1, 9), Tags({})), 1)"

    @property
    def str_representation(self) -> str:
        """Return the string representation of the constraint."""
        return f"{self.item.__class__.__name__}(1)"

    @property
    def expected_classes(self) -> set[type[Item]]:
        """Return the expected set of classes for StandardRegion."""
        return {Item, ComposedItem, Region, StandardRegion}

    def test_in(self):
        """Test the 'in' operator for the StandardRegion."""
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
