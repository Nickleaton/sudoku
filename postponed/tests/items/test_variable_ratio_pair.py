"""TestVariableRatioPair."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from postponed.src.items.pair import Pair
from src.items.region import Region
from src.items.variable_pair import VariablePair
from postponed.src.items.variable_ratio_pair import VariableRatioPair
from postponed.tests.items.test_variable_pair import TestVariablePair


class TestVariableRatioPair(TestVariablePair):
    """Test suite for the VariableRatioPair class."""

    def setUp(self) -> None:
        """Set up the board and VariableRatioPair constraint for testing."""
        super().setUp()
        self.item = VariableRatioPair(
            self.board,
            Cell.make(self.board, 1, 2),
            Cell.make(self.board, 1, 3),
            "value_variable",
        )
        self.size = 2

    @property
    def clazz(self):
        """Return the VariableRatioPair class."""
        return VariableRatioPair

    @property
    def representation(self) -> str:
        """Return the string representation of VariableRatioPair."""
        return (
            "VariableRatioPair"
            "("
            "Board(9, 9, {}), "
            "Cell(Board(9, 9, {}), 1, 2), "
            "Cell(Board(9, 9, {}), 1, 3), "
            "'value_variable'"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for VariableRatioPair."""
        return "VariableRatioPair: 12-13=value_variable"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for VariableRatioPair."""
        return {Cell, Item, Pair, VariablePair, VariableRatioPair, ComposedItem, Region}

    @property
    def has_rule(self) -> bool:
        """Return whether VariableRatioPair has start_location rule."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
