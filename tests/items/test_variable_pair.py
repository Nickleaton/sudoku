"""TestVariablePair."""
import unittest
from typing import Type

from src.board.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from src.items.variable_pair import VariablePair
from tests.items.test_pair import TestPair


class TestVariablePair(TestPair):
    """Test suite for the VariablePair class."""

    def setUp(self) -> None:
        """Set up the board and VariablePair constraint for testing."""
        super().setUp()

        # Initialize the board with dimensions 9x9 and block size 3x3
        self.board = Board(9, 9, 3, 3)
        # Create start VariablePair constraint with two cells and start value_variable string
        self.item = VariablePair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3), "value_variable")
        # Set the size of the pair to 2
        self.size = 2

    @property
    def clazz(self):
        """Return the VariablePair class."""
        return VariablePair

    @property
    def representation(self) -> str:
        """Return the string representation of VariablePair."""
        return (
            "VariablePair"
            "("
            "Board(9, 9, 3, 3, None), "
            "Cell(Board(9, 9, 3, 3, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None), 1, 3), "
            "'value_variable'"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for VariablePair."""
        return "VariablePair: 12-13=value_variable"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for VariablePair."""
        return {Cell, Item, Pair, VariablePair, ComposedItem, Region}

    @property
    def inside(self) -> Cell:
        """Return start Cell instance located at (1, 2)."""
        return Cell.make(self.board, 1, 2)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
