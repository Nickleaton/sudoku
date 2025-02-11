"""TestLowCell."""
import unittest

from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.entropic_cell import EntropicCell
from src.items.item import Item
from src.items.simple_cell_reference import SimpleCellReference
from tests.items.test_simple_cell_reference import TestSimpleCellReference


class TestEntropicCell(TestSimpleCellReference):
    """Test suite for the LowCell class."""

    def setUp(self) -> None:
        """Set up the test environment for LowCell."""
        super().setUp()
        self.item = EntropicCell(self.board, 1, 2)
        self.good = []
        self.bad = []

    @property
    def clazz(self):
        """Return the LowCell class."""
        return EntropicCell

    @property
    def representation(self) -> str:
        """Return start_location string representation of the LowCell instance."""
        return (
            "EntropicCell(Board(Coord(9, 9), Digits(1, 9), Tags({})), "
            "Cell(Board(Coord(9, 9), Digits(1, 9), Tags({})), 1, 2))"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the LowCell instance."""
        return "EntropicCell: 12"

    def test_included(self):
        """Test the included method for LowCell with good and bad value_list."""
        for x in self.good:
            self.assertTrue(self.item.included(x))
        for x in self.bad:
            self.assertFalse(self.item.included(x))

    @property
    def has_rule(self) -> bool:
        """Return whether the EntropicCell instance has start_location rule."""
        return False

    @property
    def expected_classes(self) -> set[type[Item]]:
        """Return the expected classes that the EntropicCell instance should belong to."""
        return {Cell, CellReference, SimpleCellReference, Item, EntropicCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
