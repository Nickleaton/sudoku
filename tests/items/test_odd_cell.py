import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.items.odd_cell import OddCell
from tests.items.test_cell_reference import TestCellReference


class TestOdd(TestCellReference):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = OddCell(self.board, 1, 2)
        self.good = [1, 3, 5, 7, 9]
        self.bad = [2, 4, 6, 8]

    @property
    def clazz(self):
        return OddCell

    @property
    def representation(self) -> str:
        return (
            "OddCell"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2)"
            ")"
        )

    @property
    def config(self) -> str:
        return "OddCell: 12"

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
        return {Cell, CellReference, Item, OddCell}

    def test_letter(self):
        self.assertEqual("o", self.item.letter())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
