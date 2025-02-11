"""TestEvenCell."""
import unittest

from src.items.partity_cell import ParityCell

from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.items.simple_cell_reference import SimpleCellReference
from tests.items.test_simple_cell_reference import TestSimpleCellReference


class TestParityCell(TestSimpleCellReference):
    """Test suite for the EvenCell class."""

    def setUp(self) -> None:
        """Set up the test environment by creating start_location board and initializing the EvenCell."""
        super().setUp()
        self.item = ParityCell(self.board, 1, 2)
        self.good = []
        self.bad = []
        self.letter = ''

    @property
    def clazz(self):
        """Return the EvenCell class."""
        return ParityCell

    @property
    def representation(self) -> str:
        """Return start_location string representation of the EvenCell instance."""
        return (
            "ParityCell(Board(Coord(9, 9), Digits(1, 9), Tags({})), "
            "Cell(Board(Coord(9, 9), Digits(1, 9), Tags({})), 1, 2))"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the EvenCell."""
        return "ParityCell: 12"

    def test_included(self):
        """Test the `included` method of the EvenCell class."""
        for x in self.good:
            self.assertTrue(self.item.included(x))
        for x in self.bad:
            self.assertFalse(self.item.included(x))

    @property
    def has_rule(self) -> bool:
        """Return whether the EvenCell has start_location rule."""
        return False

    @property
    def expected_classes(self) -> set[type[Item]]:
        """Return the expected classes that the EvenCell should belong to."""
        return {Cell, CellReference, SimpleCellReference, Item, ParityCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
