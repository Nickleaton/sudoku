"""TestLowCell."""
import unittest

from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.entropic_cell import EntropicCell
from src.items.item import Item
from src.items.low_cell import LowCell
from src.items.simple_cell_reference import SimpleCellReference
from tests.items.test_entropic_cell import TestEntropicCell


class TestLowCell(TestEntropicCell):
    """Test suite for the LowCell class."""

    def setUp(self) -> None:
        """Set up the test environment for LowCell."""
        super().setUp()
        self.item = LowCell(self.board, 1, 2)
        self.good = [1, 2, 3]
        self.bad = [4, 5, 6, 7, 8, 9]
        self.letter = 'l'

    @property
    def clazz(self):
        """Return the LowCell class."""
        return LowCell

    @property
    def representation(self) -> str:
        """Return start_location string representation of the LowCell instance."""
        return (
            "LowCell(Board(Coord(9, 9), Digits(1, 9), Tags({})), "
            "Cell(Board(Coord(9, 9), Digits(1, 9), Tags({})), 1, 2))"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the LowCell instance."""
        return "LowCell: 12"

    def test_included(self):
        """Test the included method for LowCell with good and bad value_list."""
        for x in self.good:
            self.assertTrue(self.item.included(x))
        for x in self.bad:
            self.assertFalse(self.item.included(x))

    @property
    def has_rule(self) -> bool:
        """Return whether the LowCell instance has start_location rule."""
        return True

    @property
    def expected_classes(self) -> set[type[Item]]:
        """Return the expected classes that the LowCell instance should belong to."""
        return {Cell, CellReference, SimpleCellReference, Item, EntropicCell, LowCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
