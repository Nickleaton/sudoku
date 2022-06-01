import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.high_cell import HighCell
from src.items.item import Item
from tests.items.test_cell_reference import TestCellReference


class TestLowCell(TestCellReference):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = HighCell(self.board, 1, 2)
        self.good = [7, 8, 9]
        self.bad = [1, 2, 3, 4, 5, 6]

    @property
    def clazz(self):
        return HighCell

    @property
    def representation(self) -> str:
        return (
            "HighCell(Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2))"
        )

    @property
    def config(self) -> str:
        return "HighCell: 12"

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
        return {Cell, CellReference, Item, HighCell}

    def test_letter(self):
        self.assertEqual("h", self.item.letter())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
