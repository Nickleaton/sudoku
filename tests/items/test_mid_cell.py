"""TestMidCell."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.items.mid_cell import MidCell
from src.items.simple_cell_reference import SimpleCellReference
from tests.items.test_simple_cell_reference import TestSimpleCellReference


class TestMidCell(TestSimpleCellReference):
    """Test suite for the MidCell class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.item = MidCell(self.board, 1, 2)
        self.good = [4, 5, 6]
        self.bad = [1, 2, 3, 7, 8, 9]
        self.letter = 'm'

    @property
    def clazz(self):
        """Return the MidCell class."""
        return MidCell

    @property
    def representation(self) -> str:
        """Return the string representation of the MidCell instance."""
        return (
            "MidCell(Board(9, 9, 3, 3, None), "
            "Cell(Board(9, 9, 3, 3, None), 1, 2))"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the MidCell instance."""
        return "MidCell: 12"

    def test_included(self):
        """Test the 'included' method to check if value_list are correctly included or excluded."""
        for x in self.good:
            self.assertTrue(self.item.included(x))
        for x in self.bad:
            self.assertFalse(self.item.included(x))

    @property
    def has_rule(self) -> bool:
        """Return whether the MidCell instance has start rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the MidCell instance should belong to."""
        return {Cell, CellReference, SimpleCellReference, Item, MidCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
