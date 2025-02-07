"""TestBoxes."""
import unittest

from src.items.box import Box
from src.items.boxes import Boxes
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.region_set import RegionSet
from src.items.standard_region import StandardRegion
from src.items.standard_region_set import StandardRegionSet
from src.utils.coord import Coord
from tests.items.test_standard_region_sets import TestStandardRegionSet


class TestBoxes(TestStandardRegionSet):
    """Test suite for the Boxes constraint in the Board."""

    def setUp(self) -> None:
        """Set up the Board and Boxes instance for testing."""
        super().setUp()
        self.item = Boxes(self.board, Coord(3, 3))
        self.size = 9

    @property
    def clazz(self):
        """Return the Boxes class."""
        return Boxes

    @property
    def config(self) -> str:
        """Return the configuration string for the Boxes constraint."""
        return "Boxes: 3x3"

    @property
    def representation(self) -> str:
        """Return the string representation for the Boxes constraint."""
        return "Boxes(Board(Coord(9, 9), Digits(1, 9), Tags({})))"

    @property
    def expected_classes(self) -> set[type[Item]]:
        """Return the expected classes that the Boxes constraint should belong to."""
        return {Item, ComposedItem, Cell, StandardRegion, Region, Box, Boxes, StandardRegion, RegionSet,
                StandardRegionSet}

    @property
    def has_rule(self) -> bool:
        """Return whether the Boxes have start_location rule associated with them."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
