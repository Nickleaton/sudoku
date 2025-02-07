"""TestDisjointGroups."""
import unittest

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.disjoint_group import DisjointGroup
from src.items.disjoint_groups import DisjointGroups
from src.items.item import Item
from src.items.region import Region
from src.items.region_set import RegionSet
from src.items.standard_region import StandardRegion
from src.items.standard_region_set import StandardRegionSet
from tests.items.test_standard_region_sets import TestStandardRegionSet


class TestDisjointGroups(TestStandardRegionSet):
    """Test suite for the DisjointGroups class."""

    def setUp(self) -> None:
        """Set up the test environment, creating the board and the DisjointGroups constraint."""
        super().setUp()
        self.item = DisjointGroups(self.board)
        self.size = 9

    @property
    def clazz(self):
        """Return the DisjointGroups class."""
        return DisjointGroups

    @property
    def config(self) -> str:
        """Return the configuration string for the DisjointGroups."""
        return "DisjointGroups:"

    @property
    def representation(self) -> str:
        """Return the string representation of the DisjointGroups constraint."""
        return "DisjointGroups(Board(Coord(9, 9), Digits(1, 9), Tags({})))"

    @property
    def expected_classes(self) -> set[type[Item]]:
        """Return the expected classes that the DisjointGroups should belong to."""
        return {Item, ComposedItem, Cell, StandardRegion, Region, DisjointGroup, DisjointGroups, RegionSet,
                StandardRegion, StandardRegionSet}

    @property
    def has_rule(self) -> bool:
        """Return whether the DisjointGroups has start_location rule."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
