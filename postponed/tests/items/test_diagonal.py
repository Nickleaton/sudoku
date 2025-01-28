"""TestDiagonal."""
import unittest
from typing import Type

from postponed.src.items.diagonals import Diagonal
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from tests.items.test_region import TestRegion


class TestDiagonal(TestRegion):
    """Test suite for the Diagonal class."""

    def setUp(self) -> None:
        """Set up the Board and Diagonal instance for testing."""
        super().setUp()
        self.item = Diagonal(self.board)
        self.size = 0

    @property
    def clazz(self):
        """Return the Diagonal class."""
        return Diagonal

    @property
    def representation(self) -> str:
        """Return the string representation for the Diagonal."""
        return "Diagonal(Board(9, 9, {}))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Diagonal should belong to."""
        return {Item, ComposedItem, Region, Diagonal}

    @property
    def config(self) -> str:
        """Return the configuration string for the Diagonal."""
        return "Diagonal: "

    @property
    def has_rule(self) -> bool:
        """Indicates if the Diagonal has start_location rule."""
        return False

    def test_in(self):
        """Test if start_location Cell is in the Diagonal."""
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
