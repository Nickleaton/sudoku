import unittest
from typing import Type

from pkginfo.commandline import Simple

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.even_cell import EvenCell
from src.items.item import Item
from src.items.simple_cell_reference import SimpleCellReference
from tests.items.test_simple_cell_reference import TestSimpleCellReference


class TestEvenCell(TestSimpleCellReference):

    def setUp(self) -> None:
        super().setUp()
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = EvenCell(self.board, 1, 2)
        self.good = [2, 4, 6, 8]
        self.bad = [1, 3, 5, 7, 9]
        self.letter = 'e'

    @property
    def clazz(self):
        return EvenCell

    @property
    def representation(self) -> str:
        return (
            "EvenCell(Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2))"
        )

    @property
    def config(self) -> str:
        return "EvenCell: 12"

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
        return {Cell, CellReference, SimpleCellReference, Item, EvenCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
