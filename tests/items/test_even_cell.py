"""TestEvenCell."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.even_cell import EvenCell
from src.items.item import Item
from src.items.simple_cell_reference import SimpleCellReference
from tests.items.test_simple_cell_reference import TestSimpleCellReference


class TestEvenCell(TestSimpleCellReference):
    """Test suite for the EvenCell class."""

    def setUp(self) -> None:
        """Set up the test environment by creating start board and initializing the EvenCell."""
        super().setUp()
        self.item = EvenCell(self.board, 1, 2)
        self.good = [2, 4, 6, 8]
        self.bad = [1, 3, 5, 7, 9]
        self.letter = 'e'

    @property
    def clazz(self):
        """Return the EvenCell class."""
        return EvenCell

    @property
    def representation(self) -> str:
        """Return start string representation of the EvenCell instance."""
        return (
            "EvenCell(Board(9, 9, 3, 3, None), "
            "Cell(Board(9, 9, 3, 3, None), 1, 2))"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the EvenCell."""
        return "EvenCell: 12"

    def test_included(self):
        """Test the `included` method of the EvenCell class."""
        for x in self.good:
            self.assertTrue(self.item.included(x))
        for x in self.bad:
            self.assertFalse(self.item.included(x))

    @property
    def has_rule(self) -> bool:
        """Return whether the EvenCell has start rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the EvenCell should belong to."""
        return {Cell, CellReference, SimpleCellReference, Item, EvenCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
