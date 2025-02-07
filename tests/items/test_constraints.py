"""TestConstraints."""
import unittest

from src.items.box import Box
from src.items.boxes import Boxes
from src.items.cell import Cell
from src.items.column import Column
from src.items.columns import Columns
from src.items.composed_item import ComposedItem
from src.items.constraints import Constraints
from src.items.item import Item
from src.items.region import Region
from src.items.region_set import RegionSet
from src.items.row import Row
from src.items.rows import Rows
from src.items.standard_region import StandardRegion
from src.items.standard_region_set import StandardRegionSet
from src.utils.coord import Coord
from tests.items.test_composed import TestComposed


class TestConstraints(TestComposed):
    """Test suite for the Constraints class."""

    def setUp(self) -> None:
        """Set up the Board and Constraints instance for testing."""
        super().setUp()
        self.item = Constraints(self.board)
        self.item.add(Columns(self.board))
        self.item.add(Rows(self.board))
        self.item.add(Boxes(self.board, Coord(3, 3)))
        self.size = 3

    @property
    def clazz(self):
        """Return the Constraints class."""
        return Constraints

    def test_construction(self):
        """Test the construction of the Constraints instance."""
        self.assertEqual(self.size, len(self.item.components))

    def test_iteration(self):
        """Test iteration over the vectors in Constraints."""
        count = 0
        for _ in self.item:
            count += 1
        self.assertEqual(self.size, count)

    @property
    def representation(self) -> str:
        """Return the string representation for the Constraints."""
        return (
            "Constraints(Board(Coord(9, 9), Digits(1, 9), Tags({})), "
            "["
            "Columns(Board(Coord(9, 9), Digits(1, 9), Tags({}))), "
            "Rows(Board(Coord(9, 9), Digits(1, 9), Tags({}))), "
            "Boxes(Board(Coord(9, 9), Digits(1, 9), Tags({})))"
            "]"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the Constraints."""
        return (
            "Constraints:\n"
            "  - Columns:\n"
            "  - Rows:\n"
            "  - Boxes: 3x3\n"
        )

    @property
    def has_rule(self) -> bool:
        """Indicates if the Constraints has start_location rule."""
        return True

    @property
    def expected_classes(self) -> set[type[Item]]:
        """Return the expected classes that the Constraints should belong to."""
        return {Box, Boxes, Cell, Column, Columns, ComposedItem, Constraints, Item, Region,
                RegionSet, Row, Rows, StandardRegion, StandardRegionSet}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
