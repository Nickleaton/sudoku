import unittest
from typing import Type, Sequence, Any, Tuple

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.item import Item
from tests.items.test_item import TestItem


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

    def test_letter(self):
        self.assertEqual('.', self.item.letter())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
