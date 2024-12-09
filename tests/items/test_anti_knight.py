"""TestAntiKnight."""
import unittest
from typing import Type, List

from src.items.anti import Anti
from src.items.anti_knight import AntiKnight
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_anti import TestAnti


class TestAntiKnight(TestAnti):
    """Test suite for the AntiKnight class."""

    def setUp(self) -> None:
        """Set up the test environment for AntiKnight.

        Initializes the board and AntiKnight constraint.
        """
        super().setUp()
        self.item = AntiKnight(self.board)
        self.size = 448

    @property
    def clazz(self) -> Type[AntiKnight]:
        """Get the class being tested.

        Returns:
            Type[AntiKnight]: The AntiKnight class.
        """
        return AntiKnight

    def test_offsets(self):
        """Test the offsets method of AntiKnight.

        Asserts that the offsets list has the expected length of 8.
        """
        self.assertEqual(8, len(self.item.offsets()))

    @property
    def representation(self) -> str:
        """Get the string representation of the AntiKnight instance.

        Returns:
            str: The string representation of the AntiKnight object.
        """
        return "AntiKnight(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Get the expected set of classes that AntiKnight should inherit from.

        Returns:
            set[Type[Item]]: A set containing the expected classes.
        """
        return {Anti, AntiKnight, Cell, ComposedItem, DifferencePair, Item, Pair, Region}

    @property
    def config(self) -> str:
        """Get the configuration string for AntiKnight.

        Returns:
            str: The configuration string for AntiKnight.
        """
        return "AntiKnight:"

    @property
    def pair_output(self) -> List:
        """Get the expected output for pairs.

        Returns:
            List: The expected pair output.
        """
        return [[2, 3], [3, 2]]

    @property
    def has_rule(self) -> bool:
        """Check if the AntiKnight rule is applied.

        Returns:
            bool: Always returns True for AntiKnight.
        """
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
