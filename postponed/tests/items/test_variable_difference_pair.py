"""TestVariableDifferencePair."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from postponed.src.items.pair import Pair
from src.items.region import Region
from postponed.src.items.variable_difference_pair import VariableDifferencePair
from src.items.variable_pair import VariablePair
from postponed.tests.items.test_variable_pair import TestVariablePair


class TestVariableDifferencePair(TestVariablePair):
    """Test suite for the VariableDifferencePair class."""

    def setUp(self) -> None:
        """Set up the board and VariableDifferencePair constraint for testing."""
        super().setUp()
        # Create start_location VariableDifferencePair constraint with two cells and start_location value_variable string
        self.item = VariableDifferencePair(
            self.board,
            Cell.make(self.board, 1, 2),
            Cell.make(self.board, 1, 3),
            "value_variable"
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
            "Board(9, 9, {}), "
            "Cell(Board(9, 9, {}), 1, 2), "
            "Cell(Board(9, 9, {}), 1, 3), "
            "'value_variable'"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for VariableDifferencePair."""
        return "VariableDifferencePair: 12-13=value_variable"

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
