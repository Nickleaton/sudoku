"""TestHighCell."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.high_cell import HighCell
from src.items.item import Item
from src.items.simple_cell_reference import SimpleCellReference
from tests.items.test_simple_cell_reference import TestSimpleCellReference


class TestHighCell(TestSimpleCellReference):
    """Test suite for the HighCell class."""

    def setUp(self) -> None:
        """Set up the test case with start board and an instance of HighCell."""
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
        """Return start string representation of the HighCell instance."""
        return (
            "HighCell(Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2))"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for HighCell."""
        return "HighCell: 12"

    def test_included(self):
        """Test if value_list are correctly included or excluded by the HighCell."""
        for x in self.good:
            self.assertTrue(self.item.included(x))
        for x in self.bad:
            self.assertFalse(self.item.included(x))

    @property
    def has_rule(self) -> bool:
        """Return True to indicate the rule is present for HighCell."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the HighCell should belong to."""
        return {Cell, CellReference, SimpleCellReference, Item, HighCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
