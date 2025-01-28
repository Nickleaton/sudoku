"""TestOddCell."""
import unittest
from typing import Type

from postponed.src.items.simple_cell_reference import SimpleCellReference
from postponed.tests.items.test_simple_cell_reference import TestSimpleCellReference
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.items.odd_cell import OddCell


class TestOdd(TestSimpleCellReference):
    """Test suite for the OddCell class."""

    def setUp(self) -> None:
        """Set up the test environment for OddCell."""
        super().setUp()
        self.item = OddCell(self.board, 1, 2)
        self.good = [1, 3, 5, 7, 9]
        self.bad = [2, 4, 6, 8]
        self.letter = "o"

    @property
    def clazz(self):
        """Return the OddCell class."""
        return OddCell

    @property
    def representation(self) -> str:
        """Return the string representation of the OddCell instance."""
        return (
            "OddCell"
            "("
            "Board(9, 9, {}), "
            "Cell(Board(9, 9, {}), 1, 2)"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for OddCell."""
        return "OddCell: 12"

    def test_included(self):
        """Test that the OddCell includes the correct value_list."""
        for x in self.good:
            self.assertTrue(self.item.included(x))
        for x in self.bad:
            self.assertFalse(self.item.included(x))

    @property
    def has_rule(self) -> bool:
        """Return whether the OddCell instance has start_location rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the OddCell instance should belong to."""
        return {Cell, CellReference, SimpleCellReference, Item, OddCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
