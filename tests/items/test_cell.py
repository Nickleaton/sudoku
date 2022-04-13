import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell, Even, Odd, Fortress, Known, CellReference
from src.items.item import Item
from tests.items.test_item import TestItem


class TestCell(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Cell(self.board, 1, 2)

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
        one = Cell(None, 1, 1)
        two = Cell(None, 2, 1)
        self.assertEqual(one, one)
        self.assertNotEqual(one, two)

    def test_lt(self):
        one = Cell(None, 1, 1)
        two = Cell(None, 2, 1)
        three = Cell(None, 2, 2)
        four = Cell(None, 3, 2)
        self.assertLess(one, two)
        self.assertLess(two, three)
        self.assertFalse(four < three)

    def test_name(self):
        self.assertIsNotNone(self.item.name)

    def test_invalid(self):
        bad = Cell(Board(9, 9), -1, -1)
        self.assertFalse(bad.valid)


class TestCellReference(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = CellReference(self.board, 1, 2)

    @property
    def representation(self) -> str:
        return (
            "CellReference"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), "
            "1, "
            "2"
            ")"
            ")"
        )

    @property
    def config(self) -> str:
        return "CellReference:\n" \
               "    Row: 1\n" \
               "    Column: 2\n"

    @property
    def has_rule(self) -> bool:
        return False

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, CellReference, Item}


class TestEven(TestCellReference):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Even(self.board, 1, 2)
        self.good = [2, 4, 6, 8]
        self.bad = [1, 3, 5, 7, 9]

    @property
    def representation(self) -> str:
        return "Even(Board(9, 9, 3, 3, None, None, None, None), Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2))"

    @property
    def config(self) -> str:
        return "Even:\n" \
               "    Row: 1\n" \
               "    Column: 2\n"

    def test_included(self):
        for x in self.good:
            self.assertTrue(self.item.included(x))
        for x in self.bad:
            self.assertFalse(self.item.included(x))

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, CellReference, Item, Even}


class TestOdd(TestCellReference):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Odd(self.board, 1, 2)
        self.good = [1, 3, 5, 7, 9]
        self.bad = [2, 4, 6, 8]

    @property
    def representation(self) -> str:
        return "Odd(Board(9, 9, 3, 3, None, None, None, None), Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2))"

    @property
    def config(self) -> str:
        return "Odd:\n" \
               "    Row: 1\n" \
               "    Column: 2\n"

    def test_included(self):
        for x in self.good:
            self.assertTrue(self.item.included(x))
        for x in self.bad:
            self.assertFalse(self.item.included(x))

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, CellReference, Item, Odd}


class TestFortress(TestCellReference):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Fortress(self.board, 1, 2)

    @property
    def representation(self) -> str:
        return (
            "Fortress("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), "
            "1, "
            "2"
            ")"
            ")"
        )

    @property
    def config(self) -> str:
        return "Fortress:\n" \
               "    Row: 1\n" \
               "    Column: 2\n"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, CellReference, Item, Fortress}


class TestKnown(TestCellReference):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Known(self.board, 1, 2, 9)

    @property
    def representation(self) -> str:
        return ("Known("
                "Board(9, 9, 3, 3, None, None, None, None), "
                "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
                "9"
                ")"
                )

    @property
    def config(self) -> str:
        return "Known:\n" \
               "    Row: 1\n" \
               "    Column: 2\n" \
               "    Digit: 9\n"

    @property
    def has_rule(self) -> bool:
        return False

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, CellReference, Item, Known}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
