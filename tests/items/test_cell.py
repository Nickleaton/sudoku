import unittest
from typing import Type, Sequence, Tuple, Any

from src.items.board import Board
from src.items.cell import Cell, CellException
from src.items.item import Item
from tests.items.test_item import TestItem


class TestCell(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Cell.make(self.board, 1, 2)

    @property
    def representation(self) -> str:
        return "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Cell}

    @property
    def config(self) -> str:
        return "Cell:\n" \
               "    Row: 1\n" \
               "    Column: 2\n"

    def test_rc(self):
        self.assertEqual((1, 2), self.item.row_column)

    def test_eq(self):
        one = Cell.make(None, 1, 1)
        two = Cell.make(None, 2, 1)
        self.assertEqual(one, one)
        self.assertNotEqual(one, two)
        with self.assertRaises(CellException):
            _ = one == "xxx"

    def test_lt(self):
        one = Cell.make(None, 1, 1)
        two = Cell.make(None, 2, 1)
        three = Cell.make(None, 2, 2)
        four = Cell.make(None, 3, 2)
        self.assertLess(one, two)
        self.assertLess(two, three)
        self.assertFalse(four < three)
        with self.assertRaises(CellException):
            _ = one < "xxx"

    def test_name(self):
        self.assertIsNotNone(self.item.name)

    def test_invalid(self):
        bad = Cell.make(Board(9, 9), -1, -1)
        self.assertFalse(bad.valid)

    def test_letter(self):
        self.assertEqual(".", self.item.letter())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
