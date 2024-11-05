import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.items.mid_cell import MidCell
from src.items.simple_cell_reference import SimpleCellReference
from tests.items.test_simple_cell_reference import TestSimpleCellReference


class TestMidCell(TestSimpleCellReference):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = MidCell(self.board, 1, 2)
        self.good = [4, 5, 6]
        self.bad = [1, 2, 3, 7, 8, 9]
        self.letter = 'm'

    @property
    def clazz(self):
        return MidCell

    @property
    def representation(self) -> str:
        return (
            "MidCell(Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2))"
        )

    @property
    def config(self) -> str:
        return "MidCell: 12"

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
        return {Cell, CellReference, SimpleCellReference, Item, MidCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
