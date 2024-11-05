import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.fortress_cell import FortressCell
from src.items.item import Item
from src.items.simple_cell_reference import SimpleCellReference
from tests.items.test_simple_cell_reference import TestSimpleCellReference


class TestFortressCell(TestSimpleCellReference):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = FortressCell(self.board, 1, 2)
        self.letter = 'f'

    @property
    def clazz(self):
        return FortressCell

    @property
    def representation(self) -> str:
        return (
            "FortressCell("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), "
            "1, "
            "2"
            ")"
            ")"
        )

    @property
    def config(self) -> str:
        return "FortressCell: 12"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, CellReference, SimpleCellReference, Item, FortressCell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
