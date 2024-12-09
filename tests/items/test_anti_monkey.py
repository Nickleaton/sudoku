"""TestAntiMonkey."""
import unittest
from typing import Type, List

from src.items.anti import Anti
from src.items.anti_monkey import AntiMonkey
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_anti import TestAnti


class TestAntiMonkey(TestAnti):
    """Test suite for the AntiMonkey class."""

    def setUp(self) -> None:
        """Set up the test environment for AntiMonkey.

        Initializes the board and AntiMonkey constraint.
        """
        super().setUp()
        Cell.make_board(self.board)
        self.item = AntiMonkey(self.board)
        self.size = 384

    @property
    def clazz(self) -> Type[AntiMonkey]:
        """Get the class being tested.

        Returns:
            Type[AntiMonkey]: The AntiMonkey class.
        """
        return AntiMonkey

    def test_offsets(self):
        """Test the offsets method of AntiMonkey.

        Asserts that the offsets list has the expected length of 8.
        """
        self.assertEqual(8, len(self.item.offsets()))

    @property
    def representation(self) -> str:
        """Get the string representation of the AntiMonkey instance.

        Returns:
            str: The string representation of the AntiMonkey object.
        """
        return "AntiMonkey(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Get the expected set of classes that AntiMonkey should inherit from.

        Returns:
            set[Type[Item]]: A set containing the expected classes.
        """
        return {Anti, AntiMonkey, Cell, ComposedItem, DifferencePair, Item, Pair, Region}

    @property
    def config(self) -> str:
        """Get the configuration string for AntiMonkey.

        Returns:
            str: The configuration string for AntiMonkey.
        """
        return "AntiMonkey:"

    @property
    def pair_output(self) -> List:
        """Get the expected output for pairs.

        Returns:
            List: The expected pair output.
        """
        return [[2, 4], [4, 2]]

    @property
    def has_rule(self) -> bool:
        """Check if the AntiMonkey rule is applied.

        Returns:
            bool: Always returns True for AntiMonkey.
        """
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
