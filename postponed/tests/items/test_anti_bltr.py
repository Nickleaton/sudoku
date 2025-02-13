"""TestAntiBltr."""
import unittest
from typing import Type

from postponed.src.items.anti_bltr import AntiBLTR
from postponed.src.items.anti_diagonal import AntiDiagonal
from postponed.src.items.diagonals import Diagonal
from postponed.tests.items.test_anti_diagonal import TestAntiDiagonal
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestAntiBLTR(TestAntiDiagonal):
    """Test suite for the AntiBLTR class."""

    def setUp(self) -> None:
        """Set up the test environment for AntiBLTR.

        Initializes the board and AntiBLTR constraint.
        """
        super().setUp()
        self.item = AntiBLTR(self.board)
        self.size = 9
        self.constraints.add(self.item)

    @property
    def clazz(self) -> Type[AntiBLTR]:
        """Get the class being tested.

        Returns:
            Type[AntiBLTR]: The AntiBLTR class.
        """
        return AntiBLTR

    @property
    def representation(self) -> str:
        """Get the string representation of the AntiBLTR instance.

        Returns:
            str: The string representation of the AntiBLTR object.
        """
        return "AntiBLTR(Board(9, 9, {}))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Get the expected set of classes that AntiBLTR should inherit from.

        Returns:
            set[Type[Item]]: A set containing the expected classes.
        """
        return {Item, ComposedItem, Cell, Region, Diagonal, AntiBLTR, AntiDiagonal}

    @property
    def config(self) -> str:
        """Get the configuration string for AntiBLTR.

        Returns:
            str: The configuration string for AntiBLTR.
        """
        return "AntiBLTR:"

    def test_in(self):
        """Test the containment of cells in AntiBLTR.

        Asserts that certain cells are contained within the AntiBLTR constraint and others are not.
        """
        self.assertIn(Cell.make(self.board, 5, 5), self.item)
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
