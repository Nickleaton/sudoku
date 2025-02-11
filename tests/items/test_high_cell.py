"""TestMidCell."""
import unittest

from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.entropic_cell import EntropicCell
from src.items.high_cell import HighCell
from src.items.item import Item
from src.items.simple_cell_reference import SimpleCellReference
from tests.items.test_entropic_cell import TestEntropicCell


class TestHighCell(TestEntropicCell):
    """Test suite for the MidCell class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.item = HighCell(self.board, 1, 2)
        self.good = [7, 8, 9]
        self.bad = [1, 2, 3, 4, 5, 6]
        self.letter = 'h'

    @property
    def clazz(self):
        """Return the HighCell class."""
        return HighCell

    @property
    def representation(self) -> str:
        """Return the string representation of the HighCell instance."""
        return (
            "HighCell(Board(Coord(9, 9), Digits(1, 9), Tags({})), "
            "Cell(Board(Coord(9, 9), Digits(1, 9), Tags({})), 1, 2))"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the MidCell instance."""
        return "HighCell: 12"

    def test_included(self):
        """Test the 'included' method to check if value_list are correctly included or excluded."""
        for x in self.good:
            self.assertTrue(self.item.included(x))
        for x in self.bad:
            self.assertFalse(self.item.included(x))

    @property
    def has_rule(self) -> bool:
        """Return whether the HighCell instance has start_location rule."""
        return True

    @property
    def expected_classes(self) -> set[type[Item]]:
        """Return the expected classes that the MidCell instance should belong to."""
        return {Cell, CellReference, SimpleCellReference, Item, EntropicCell, HighCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
