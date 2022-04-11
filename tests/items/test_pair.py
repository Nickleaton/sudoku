import unittest
from typing import Type

import oyaml as yaml

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.pair import Pair
from tests.items.test_item import TestItem


class TestPair(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Pair(self.board, Cell(None, 1, 2), Cell(None, 1, 3))

    @property
    def representation(self) -> str:
        return f"Pair(Board(9, 9, 3, 3, None, None, None, None), Cell(None, 1, 2), Cell(None, 1, 3))"

    @property
    def config(self):
        return f"[[1, 2], [1, 3]]"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Item, Pair}

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.item.__class__.__name__, self.board, data)
        self.assertIsNotNone(item)
        self.assertEqual(self.item.__class__, item.__class__)

    def test_difference(self):
        self.assertIsNone(self.item.difference)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
