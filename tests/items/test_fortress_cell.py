"""TestFortressCell."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.fortress_cell import FortressCell
from src.items.item import Item
from src.items.simple_cell_reference import SimpleCellReference
from tests.items.test_simple_cell_reference import TestSimpleCellReference


class TestFortressCell(TestSimpleCellReference):
    """Test suite for the FortressCell class."""

    def setUp(self) -> None:
        """Set up the test environment by creating a board and initializing the FortressCell item."""
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = FortressCell(self.board, 1, 2)
        self.letter = 'f'

    @property
    def clazz(self):
        """Return the FortressCell class."""
        return FortressCell

    @property
    def representation(self) -> str:
        """Return a string representation of the FortressCell instance."""
        return (
            "FortressCell("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), "
            "1, "
            "2"
            ")"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the FortressCell."""
        return "FortressCell: 12"

    @property
    def has_rule(self) -> bool:
        """Return True to indicate the rule is present for the FortressCell."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the FortressCell should belong to."""
        return {Cell, CellReference, SimpleCellReference, Item, FortressCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
