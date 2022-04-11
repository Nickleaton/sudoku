import unittest
from typing import Type

import oyaml as yaml

from src.items.board import Board
from src.items.frame import Frame
from src.items.item import Item
from src.utils.side import Side
from tests.items.test_item import TestItem


class TestFrame(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Frame(self.board, Side.TOP, 1, 20)
        self.size = 9

    @property
    def representation(self) -> str:
        return "Frame(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, 20)"

    @property
    def config(self):
        return "T1=20"

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.item.__class__.__name__, self.board, data)
        self.assertIsNotNone(item)
        self.assertEqual(self.item.__class__, item.__class__)

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Frame, Item}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
