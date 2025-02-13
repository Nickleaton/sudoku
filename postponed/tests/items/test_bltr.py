"""TestBltr."""
import unittest
from typing import Type

from postponed.src.items.bltr import BLTR
from postponed.src.items.diagonals import Diagonal
from postponed.src.items.standard_diagonal import StandardDiagonal
from postponed.tests.items.test_standard_diagonal import TestStandardDiagonal
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestBLTR(TestStandardDiagonal):
    """Test suite for the BLTR class."""

    def setUp(self) -> None:
        """Set up the board and constraint for testing."""
        super().setUp()

        self.item = BLTR(self.board)
        self.size = 9

    @property
    def clazz(self) -> Type[BLTR]:
        """Get the class being tested.

        Returns:
            Type[BLTR]: The BLTR class.
        """
        return BLTR

    @property
    def representation(self) -> str:
        """Get the string representation of the BLTR constraint.

        Returns:
            str: The string representation of the BLTR constraint.
        """
        return "BLTR(Board(9, 9, {}))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Get the expected set of classes that BLTR should inherit from.

        Returns:
            set[Type[Item]]: A set containing the expected classes.
        """
        return {Item, ComposedItem, Cell, Region, Diagonal, StandardDiagonal, BLTR}

    @property
    def config(self) -> str:
        """Get the configuration string for BLTR.

        Returns:
            str: The configuration string for BLTR.
        """
        return "BLTR:"

    def test_in(self):
        """Test if start_location cell is contained within the BLTR constraint.

        Verifies that start_location cell at (5, 5) is contained within the BLTR constraint,
        but start_location cell at (1, 2) is not.
        """
        self.assertIn(Cell.make(self.board, 5, 5), self.item)
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
