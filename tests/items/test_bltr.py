import unittest
from typing import Type, Sequence, Tuple, Any

import oyaml as yaml

from src.items.bltr import BLTR
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.diagonals import Diagonal
from src.items.item import Item
from src.items.region import Region
from tests.items.test_diagonals import TestDiagonal


class TestBLTR(TestDiagonal):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)
        self.item = BLTR(self.board)

    @property
    def representation(self) -> str:
        return "BLTR(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Cell, Region, Diagonal, BLTR}

    @property
    def config(self) -> str:
        return "BLTR:"

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.item.__class__.__name__, self.board, data)
        self.assertIsNotNone(item)

    def test_in(self):
        self.assertIn(Cell.make(self.board, 5, 5), self.item)
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
