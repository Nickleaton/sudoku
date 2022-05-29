import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.items.pencil_mark import PencilMarkCell
from tests.items.test_cell_reference import TestCellReference


class TestPencilMarkCell(TestCellReference):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = PencilMarkCell(self.board, 1, 2, [2, 4, 6, 8])

    @property
    def clazz(self):
        return PencilMarkCell

    @property
    def representation(self) -> str:
        return (
            "PencilMarkCell(Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "[2, 4, 6, 8]"
            ")"
        )

    @property
    def config(self) -> str:
        return "PencilMarkCell: 12=2468"

    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, CellReference, Item, PencilMarkCell}

    def test_letter(self):
        self.assertEqual(".", self.item.letter())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
