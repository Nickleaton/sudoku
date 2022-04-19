import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.fortress_cell import FortressCell
from src.items.item import Item
from tests.items.test_cell_reference import TestCellReference


class TestFortressCell(TestCellReference):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = FortressCell(self.board, 1, 2)

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
        return "FortressCell:\n" \
               "    Row: 1\n" \
               "    Column: 2\n"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, CellReference, Item, FortressCell}

    def test_letter(self):
        self.assertEqual("f", self.item.letter())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
