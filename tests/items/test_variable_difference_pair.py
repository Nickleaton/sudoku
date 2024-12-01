"""TestVariableDifferencePair."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from src.items.variable_difference_pair import VariableDifferencePair
from src.items.variable_pair import VariablePair
from tests.items.test_variable_pair import TestVariablePair


class TestVariableDifferencePair(TestVariablePair):
    """Test suite for the VariableDifferencePair class."""

    def setUp(self) -> None:
        """Set up the board and VariableDifferencePair item for testing."""
        # Initialize the board with dimensions 9x9 and block size 3x3
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        # Create a VariableDifferencePair item with two cells and a variable string
        self.item = VariableDifferencePair(
            self.board,
            Cell.make(self.board, 1, 2),
            Cell.make(self.board, 1, 3),
            "variable"
        )
        # Set the size of the pair to 2
        self.size = 2

    @property
    def clazz(self):
        """Return the VariableDifferencePair class."""
        return VariableDifferencePair

    @property
    def representation(self) -> str:
        """Return the string representation of VariableDifferencePair."""
        return (
            "VariableDifferencePair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3), "
            "'variable'"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for VariableDifferencePair."""
        return "VariableDifferencePair: 12-13=variable"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for VariableDifferencePair."""
        return {Cell, Item, Pair, VariablePair, VariableDifferencePair, ComposedItem, Region}

    @property
    def has_rule(self) -> bool:
        """Return whether the rule applies for VariableDifferencePair."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
