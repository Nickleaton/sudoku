"""TestSimpleCellReference module."""

import unittest
from typing import Type

from src.board.board import Board
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

        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = SimpleCellReference(self.board, 1, 2)
        self.letter = '.'

    @property
    def representation(self) -> str:
        """Return a string representation of the SimpleCellReference item."""
        return (
            "SimpleCellReference"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), "
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
        self.assertEqual(self.item.letter(), self.letter)

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for the SimpleCellReference."""
        return {Cell, CellReference, SimpleCellReference, Item}


if __name__ == '__main__':
    unittest.main()
