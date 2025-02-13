"""TestSimpleCellReference module."""

import unittest

from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.items.simple_cell_reference import SimpleCellReference
from tests.items.test_cell_reference import TestCellReference


class TestSimpleCellReference(TestCellReference):
    """Test suite for the SimpleCellReference class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.item = SimpleCellReference(self.board, 1, 2)
        self.letter = '.'

    @property
    def representation(self) -> str:
        """Return start_location string representation of the SimpleCellReference constraint."""
        return (
            "SimpleCellReference"
            "("
            "Board(Coord(9, 9), Digits(1, 9), Tags({})), "
            "Cell(Board(Coord(9, 9), Digits(1, 9), Tags({})), "
            "1, "
            "2"
            ")"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the SimpleCellReference."""
        return "SimpleCellReference: 12"

    @property
    def clazz(self):
        """Return the SimpleCellReference class."""
        return SimpleCellReference

    def test_letter(self):
        """Test the letter method of SimpleCellReference."""
        self.assertEqual(self.letter, self.item.letter())

    @property
    def expected_classes(self) -> set[type[Item]]:
        """Return the expected set of classes for the SimpleCellReference."""
        return {Cell, CellReference, SimpleCellReference, Item}


if __name__ == '__main__':
    unittest.main()
