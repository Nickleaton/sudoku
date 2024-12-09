"""TestAntiQueens."""
import unittest
from typing import Type, List

from src.items.anti import Anti
from src.items.anti_queens import AntiQueens
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_anti import TestAnti


class TestAntiQueens(TestAnti):
    """Test suite for the AntiQueens class."""

    def setUp(self) -> None:
        """Set up the test environment for AntiQueens.

        Initializes the board and AntiQueens constraint with specified columns [8, 9].
        """
        super().setUp()
        Cell.make_board(self.board)
        self.item = AntiQueens(self.board, [8, 9])
        self.size = 816

    @property
    def clazz(self) -> Type[AntiQueens]:
        """Get the class being tested.

        Returns:
            Type[AntiQueens]: The AntiQueens class.
        """
        return AntiQueens

    def test_offsets(self):
        """Test the offsets method of AntiQueens.

        Asserts that the offsets list has the expected length of 36.
        """
        self.assertEqual(36, len(self.item.offsets()))

    @property
    def config(self) -> str:
        """Get the configuration string for AntiQueens.

        Returns:
            str: The configuration string for AntiQueens.
        """
        return "AntiQueens: 8, 9"

    @property
    def representation(self) -> str:
        """Get the string representation of the AntiQueens instance.

        Returns:
            str: The string representation of the AntiQueens object.
        """
        return "AntiQueens(Board(9, 9, 3, 3, None, None, None, None), [8, 9])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Get the expected set of classes that AntiQueens should inherit from.

        Returns:
            set[Type[Item]]: A set containing the expected classes.
        """
        return {Anti, AntiQueens, Cell, ComposedItem, DifferencePair, Item, Pair, Region}

    @property
    def pair_output(self) -> List:
        """Get the expected output for pairs.

        Returns:
            List: The expected pair output.
        """
        return [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]

    @property
    def has_rule(self) -> bool:
        """Check if the AntiQueens rule is applied.

        Returns:
            bool: Always returns True for AntiQueens.
        """
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
