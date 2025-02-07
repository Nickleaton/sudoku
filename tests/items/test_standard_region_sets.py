"""TestStandardRegionSet module."""

import unittest

from postponed.tests.items.test_region_sets import TestRegionSet
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region_set import RegionSet
from src.items.standard_region_set import StandardRegionSet


class TestStandardRegionSet(TestRegionSet):
    """Test suite for the StandardRegionSet class."""

    def setUp(self) -> None:
        """Set up the test environment for StandardRegionSet."""
        super().setUp()
        self.item = StandardRegionSet(self.board, [])
        self.size = 0

    @property
    def clazz(self):
        """Return the StandardRegionSet class."""
        return StandardRegionSet

    @property
    def config(self) -> str:
        """Return the configuration string for StandardRegionSet."""
        return "StandardRegionSet:"

    @property
    def representation(self) -> str:
        """Return the string representation of StandardRegionSet."""
        return "StandardRegionSet(Board(Coord(9, 9), Digits(1, 9), Tags({})), [])"

    @property
    def expected_classes(self) -> set[type[Item]]:
        """Return the expected set of classes for StandardRegionSet."""
        return {Item, ComposedItem, RegionSet, StandardRegionSet}

    @property
    def has_rule(self) -> bool:
        """Return whether the StandardRegionSet has start_location rule."""
        return False


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
