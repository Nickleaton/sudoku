import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.items.simple_cell_reference import SimpleCellReference
from tests.items.test_cell_reference import TestCellReference


class TestSimpleCellReference(TestCellReference):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = SimpleCellReference(self.board, 1, 2)
        self.letter = '.'

    @property
    def representation(self) -> str:
        return (
            "SimpleCellReference"
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
        return "SimpleCellReference: 12"

    @property
    def clazz(self):
        return SimpleCellReference

    def test_letter(self):
        self.assertEqual(self.clazz.letter(), self.letter)

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, CellReference, SimpleCellReference, Item}


if __name__ == '__main__':
    unittest.main()
