"""TestCell module."""

import unittest
from typing import Type

from src.board.board import Board
from src.items.cell import Cell, CellException
from src.items.item import Item
from tests.items.test_item import TestItem


class TestCell(TestItem):
    """Test case for Cell class."""

    def setUp(self) -> None:
        """Set up the test case by clearing cache and initializing start Board and Cell constraint."""
        super().setUp()
        Cell.clear()
        self.item = Cell.make(self.board, 1, 2)

    @property
    def clazz(self):
        """Return the Cell class."""
        return Cell

    @property
    def representation(self) -> str:
        """Return the string representation of the Cell constraint."""
        return "Cell(Board(9, 9, 3, 3, None), 1, 2)"

    @property
    def str_representation(self) -> str:
        """Return the simplified string representation of the Cell constraint."""
        return "Cell(1, 2)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for Cell."""
        return {Item, Cell}

    @property
    def config(self) -> str:
        """Return the configuration string for Cell."""
        return "Cell: 12"

    def test_rc(self):
        """Test the row_column property of the Cell."""
        self.assertEqual((1, 2), self.item.row_column)

    def test_eq(self):
        """Test the equality comparison of the Cell."""
        one = Cell.make(self.board, 1, 1)
        two = Cell.make(self.board, 2, 1)
        self.assertEqual(one, one)
        self.assertNotEqual(one, two)
        self.assertNotEqual("xxx", one)

    def test_lt(self):
        """Test the less-than comparison of the Cell."""
        one = Cell.make(self.board, 1, 1)
        two = Cell.make(self.board, 2, 1)
        three = Cell.make(self.board, 2, 2)
        four = Cell.make(self.board, 3, 2)
        self.assertLess(one, two)
        self.assertLess(two, three)
        self.assertFalse(four < three)
        with self.assertRaises(CellException):
            _ = one < "xxx"

    def test_name(self):
        """Test the name property of the Cell."""
        self.assertIsNotNone(self.item.name)

    def test_invalid(self):
        """Test the validity of the Cell with invalid coordinates."""
        bad = Cell.make(Board(9, 9), -1, -1)
        self.assertFalse(bad.valid)

    def test_letter(self):
        """Test the letter representation of the Cell."""
        self.assertEqual(".", self.item.letter())

    def test_regions(self):
        """Test the regions method of the Cell's top-level region."""
        self.assertIsNotNone(self.item.top.regions())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
