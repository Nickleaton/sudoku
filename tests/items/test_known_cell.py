import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.items.known_cell import KnownCell
from tests.items.test_cell_reference import TestCellReference


class TestKnownCell(TestCellReference):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = KnownCell(self.board, 1, 2, 9)

    @property
    def clazz(self):
        return KnownCell

    @property
    def representation(self) -> str:
        return ("KnownCell("
                "Board(9, 9, 3, 3, None, None, None, None), "
                "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
                "9"
                ")"
                )

    @property
    def config(self) -> str:
        return "KnownCell: 12=9"

    @property
    def has_rule(self) -> bool:
        return False

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, CellReference, Item, KnownCell}

    def test_letter(self):
        self.assertEqual("9", self.item.letter())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
