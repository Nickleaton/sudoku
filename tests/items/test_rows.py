"""TestRows module."""

import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.region_set import RegionSet
from src.items.row import Row
from src.items.rows import Rows
from src.items.standard_region import StandardRegion
from src.items.standard_region_set import StandardRegionSet
from tests.items.test_standard_region_sets import TestStandardRegionSet


class TestRows(TestStandardRegionSet):
    """Test suite for the Rows class."""

    def setUp(self) -> None:
        """Set up the test environment for Rows."""
        super().setUp()
        self.item = Rows(self.board)
        self.size = 9

    @property
    def clazz(self):
        """Return the Rows class."""
        return Rows

    @property
    def config(self) -> str:
        """Return the configuration string for the Rows instance."""
        return "Rows:"

    @property
    def representation(self) -> str:
        """Return the string representation of the Rows instance."""
        return "Rows(Board(9, 9, {}))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes the Rows instance should belong to."""
        return {
            Item,
            ComposedItem,
            Cell,
            StandardRegion,
            Region,
            Row,
            Rows,
            StandardRegion,
            RegionSet,
            StandardRegionSet
        }

    @property
    def has_rule(self) -> bool:
        """Return whether the Rows instance has an associated rule."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
