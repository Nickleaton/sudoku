import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell, CellException
from src.items.item import Item
from tests.items.test_item import TestItem


class TestCell(TestItem):

    def setUp(self) -> None:
        # Need to clear cache otherwise you can get side effects from old cells.
        Cell.clear()
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Cell.make(self.board, 1, 2)

    @property
    def clazz(self):
        return Cell

    @property
    def representation(self) -> str:
        return "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Cell}

    @property
    def config(self) -> str:
        return "Cell: 12"

    def test_rc(self):
        self.assertEqual((1, 2), self.item.row_column)

    def test_eq(self):
        one = Cell.make(self.board, 1, 1)
        two = Cell.make(self.board, 2, 1)
        self.assertEqual(one, one)
        self.assertNotEqual(one, two)
        with self.assertRaises(CellException):
            _ = one == "xxx"

    def test_lt(self):
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
        self.assertIsNotNone(self.item.name)

    def test_invalid(self):
        bad = Cell.make(Board(9, 9), -1, -1)
        self.assertFalse(bad.valid)

    def test_letter(self):
        self.assertEqual(".", self.item.letter())

    def test_set_possible(self):
        cell = Cell.make(self.board, 1, 2)
        cell.set_possible([2, 4, 5])
        self.assertTrue(cell.is_possible(2))
        self.assertFalse(cell.is_possible(9))

    def test_set_impossible(self):
        cell = Cell.make(self.board, 1, 2)
        cell.set_impossible([2, 4, 5])
        self.assertTrue(cell.is_possible(3))
        self.assertFalse(cell.is_possible(2))

    def test_set_odd(self):
        cell = Cell.make(self.board, 1, 2)
        cell.set_odd()
        self.assertTrue(cell.is_possible(1))
        self.assertFalse(cell.is_possible(2))

    def test_set_even(self):
        cell = Cell.make(self.board, 1, 2)
        cell.set_even()
        self.assertFalse(cell.is_possible(1))
        self.assertTrue(cell.is_possible(2))

    def test_set_minimum(self):
        cell = Cell.make(self.board, 1, 2)
        cell.set_minimum(5)
        self.assertFalse(cell.is_possible(1))
        self.assertTrue(cell.is_possible(5))
        self.assertTrue(cell.is_possible(9))

    def test_set_maximum(self):
        cell = Cell.make(self.board, 1, 2)
        cell.set_maximum(5)
        self.assertTrue(cell.is_possible(5))
        self.assertFalse(cell.is_possible(9))

    def test_set_range(self):
        cell = Cell.make(self.board, 1, 2)
        cell.set_range(3, 6)
        self.assertFalse(cell.is_possible(1))
        self.assertTrue(cell.is_possible(5))
        self.assertFalse(cell.is_possible(9))

    def test_fixed(self):
        cell = Cell.make(self.board, 1, 2)
        self.assertFalse(cell.fixed())
        cell.set_possible([1])
        self.assertTrue(cell.fixed())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
