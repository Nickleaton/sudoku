"""TestAntiDiagonal."""
import unittest
from typing import Type

from postponed.src.items.anti_diagonal import AntiDiagonal
from postponed.src.items.diagonals import Diagonal
from postponed.tests.items.test_diagonal import TestDiagonal
from src.items.boxes import Boxes
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.constraints import Constraints
from src.items.item import Item
from src.items.region import Region


class TestAntiDiagonal(TestDiagonal):
    """Test suite for the AntiDiagonal class."""

    def setUp(self) -> None:
        """Set up the test environment for AntiDiagonal.

        Initializes the board and AntiDiagonal constraint.
        """
        super().setUp()
        self.item = AntiDiagonal(self.board)
        self.size = 0
        self.constraints = Constraints(self.board)
        self.constraints.add(Boxes(self.board, 3, 3))

    @property
    def clazz(self) -> Type[AntiDiagonal]:
        """Get the class being tested.

        Returns:
            Type[AntiDiagonal]: The AntiDiagonal class.
        """
        return AntiDiagonal

    @property
    def representation(self) -> str:
        """Get the string representation of the AntiDiagonal instance.

        Returns:
            str: The string representation of the AntiDiagonal object.
        """
        return "AntiDiagonal(Board(9, 9, {}))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Get the expected set of classes that AntiDiagonal should inherit from.

        Returns:
            set[Type[Item]]: A set containing the expected classes.
        """
        return {Item, ComposedItem, Region, Diagonal, AntiDiagonal}

    @property
    def config(self) -> str:
        """Get the configuration string for AntiDiagonal.

        Returns:
            str: The configuration string for AntiDiagonal.
        """
        return "AntiDiagonal: "

    @property
    def has_rule(self) -> bool:
        """Check if the AntiDiagonal rule is applied.

        Returns:
            bool: Always returns True for AntiDiagonal.
        """
        return True

    def test_in(self):
        """Test the containment of cells in AntiDiagonal.

        Asserts that start_location specific cell is not contained within the AntiDiagonal constraint.
        """
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
