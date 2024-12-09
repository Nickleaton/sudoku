"""TestStandardDiagonal module."""

import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.diagonals import Diagonal
from src.items.item import Item
from src.items.region import Region
from src.items.standard_diagonal import StandardDiagonal
from tests.items.test_diagonal import TestDiagonal


class TestStandardDiagonal(TestDiagonal):
    """Test suite for the StandardDiagonal class."""

    def setUp(self) -> None:
        """Set up the test environment for StandardDiagonal."""
        super().setUp()

        self.item = StandardDiagonal(self.board)
        self.size = 0

    @property
    def clazz(self):
        """Return the StandardDiagonal class."""
        return StandardDiagonal

    @property
    def representation(self) -> str:
        """Return the string representation of the StandardDiagonal."""
        return "StandardDiagonal(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for the StandardDiagonal."""
        return {Item, ComposedItem, Region, Diagonal, StandardDiagonal}

    @property
    def config(self) -> str:
        """Return the configuration string for the StandardDiagonal."""
        return "StandardDiagonal: "

    @property
    def has_rule(self) -> bool:
        """Return whether the StandardDiagonal has start rule."""
        return True

    def test_in(self):
        """Test the 'in' operator for the StandardDiagonal."""
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
