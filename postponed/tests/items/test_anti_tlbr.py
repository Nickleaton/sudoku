"""TestAntiTLBR."""
import unittest
from typing import Type

from postponed.src.items.anti_diagonal import AntiDiagonal
from postponed.src.items.anti_tlbr import AntiTLBR
from postponed.src.items.diagonals import Diagonal
from postponed.tests.items.test_anti_diagonal import TestAntiDiagonal
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestAntiTLBR(TestAntiDiagonal):
    """Test suite for the AntiTLBR class."""

    def setUp(self) -> None:
        """Set up the test environment for AntiTLBR.

        Initializes the board and AntiTLBR constraint with the default configuration.
        """
        super().setUp()
        self.item = AntiTLBR(self.board)
        self.size = 9
        self.constraints.add(self.item)


    @property
    def clazz(self) -> Type[AntiTLBR]:
        """Get the class being tested.

        Returns:
            Type[AntiTLBR]: The AntiTLBR class.
        """
        return AntiTLBR

    @property
    def representation(self) -> str:
        """Get the string representation of the AntiTLBR instance.

        Returns:
            str: The string representation of the AntiTLBR object.
        """
        return "AntiTLBR(Board(9, 9, {}))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Get the expected set of classes that AntiTLBR should inherit from.

        Returns:
            set[Type[Item]]: A set containing the expected classes.
        """
        return {Item, ComposedItem, Cell, Region, Diagonal, AntiTLBR, AntiDiagonal}

    @property
    def config(self) -> str:
        """Get the configuration string for AntiTLBR.

        Returns:
            str: The configuration string for AntiTLBR.
        """
        return "AntiTLBR:"

    def test_in(self):
        """Test the inclusion of cells in the AntiTLBR constraint.

        Asserts that start_location specific cell is included and another is not.
        """
        self.assertIn(Cell.make(self.board, 5, 5), self.item)
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
