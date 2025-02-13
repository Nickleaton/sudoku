"""TestGirandola."""
import unittest
from typing import Type

from postponed.src.items.girandola import Girandola
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.special_region import SpecialRegion
from tests.items.test_special_region import TestSpecialRegion


class TestGirandola(TestSpecialRegion):
    """Test suite for the Girandola class."""

    def setUp(self) -> None:
        """Set up the test case with start_location board and an instance of Girandola."""
        super().setUp()
        self.item = Girandola(self.board)
        self.size = 9

    @property
    def clazz(self):
        """Return the Girandola class."""
        return Girandola

    @property
    def config(self) -> str:
        """Return the configuration string for the Girandola."""
        return "Girandola:"

    @property
    def representation(self) -> str:
        """Return start_location string representation of the Girandola instance."""
        return "Girandola(Board(9, 9, {}))"

    @property
    def has_rule(self) -> bool:
        """Return True to indicate the rule is present for Girandola."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Girandola should belong to."""
        return {Item, ComposedItem, Cell, Region, Girandola, SpecialRegion}

    def test_in(self):
        """Test if the cell is inside the Girandola region."""
        self.assertIn(Cell.make(self.board, 1, 1), self.item)
        self.assertNotIn(Cell.make(self.board, 8, 8), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
