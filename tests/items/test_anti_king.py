"""TestAntiKing."""
import unittest
from typing import Type, List

from src.items.anti import Anti
from src.items.anti_king import AntiKing
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_anti import TestAnti


class TestAntiKing(TestAnti):
    """Test suite for the AntiKing class."""

    def setUp(self) -> None:
        """Set up the test environment for AntiKing.

        Initializes the board and AntiKing item.
        """
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        Cell.make_board(self.board)
        self.item = AntiKing(self.board)
        self.size = 544

    @property
    def clazz(self) -> Type[AntiKing]:
        """Get the class being tested.

        Returns:
            Type[AntiKing]: The AntiKing class.
        """
        return AntiKing

    def test_offsets(self):
        """Test the offsets method of AntiKing.

        Asserts that the offsets list has the expected length of 8.
        """
        self.assertEqual(8, len(self.item.offsets()))

    @property
    def representation(self) -> str:
        """Get the string representation of the AntiKing instance.

        Returns:
            str: The string representation of the AntiKing object.
        """
        return "AntiKing(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Get the expected set of classes that AntiKing should inherit from.

        Returns:
            set[Type[Item]]: A set containing the expected classes.
        """
        return {Anti, AntiKing, Cell, ComposedItem, DifferencePair, Item, Pair, Region}

    @property
    def config(self) -> str:
        """Get the configuration string for AntiKing.

        Returns:
            str: The configuration string for AntiKing.
        """
        return "AntiKing:"

    @property
    def pair_output(self) -> List:
        """Get the expected output for pairs.

        Returns:
            List: The expected pair output.
        """
        return [[2, 2], [1, 2], [2, 1]]

    @property
    def has_rule(self) -> bool:
        """Check if the AntiKing rule is applied.

        Returns:
            bool: Always returns True for AntiKing.
        """
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
