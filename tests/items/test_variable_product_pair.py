"""TestVariableProductPair."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from src.items.variable_pair import VariablePair
from src.items.variable_product_pair import VariableProductPair
from tests.items.test_variable_pair import TestVariablePair


class TestVariableProductPair(TestVariablePair):
    """Test suite for the VariableProductPair class."""

    def setUp(self) -> None:
        """Set up the board and VariableProductPair constraint for testing."""
        super().setUp()
        # Create start VariableProductPair constraint with two cells and start value_variable string
        self.item = VariableProductPair(
            self.board,
            Cell.make(self.board, 1, 2),
            Cell.make(self.board, 1, 3),
            "value_variable"
        )
        # Set the size of the product pair to 2
        self.size = 2

    @property
    def clazz(self):
        """Return the VariableProductPair class."""
        return VariableProductPair

    @property
    def representation(self) -> str:
        """Return the string representation of VariableProductPair."""
        return (
            "VariableProductPair"
            "("
            "Board(9, 9, 3, 3, None), "
            "Cell(Board(9, 9, 3, 3, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None), 1, 3), "
            "'value_variable'"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for VariableProductPair."""
        return "VariableProductPair: 12-13=value_variable"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for VariableProductPair."""
        return {Cell, Item, Pair, VariablePair, VariableProductPair, ComposedItem, Region}

    @property
    def has_rule(self) -> bool:
        """Return whether VariableProductPair has start rule."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
