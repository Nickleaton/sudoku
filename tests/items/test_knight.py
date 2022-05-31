import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.knight import Knight
from tests.items.test_composed import TestComposed
from tests.items.test_item import TestItem


class TestKnight(TestComposed):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Knight(self.board, [2, 4, 6, 8])
        self.size = 81

    @property
    def clazz(self):
        return Knight

    @property
    def has_rule(self) -> bool:
        return True

    def test_offsets(self):
        self.assertEqual(8, len(self.item.offsets()))

    @property
    def config(self) -> str:
        return "Knight: 2, 4, 6, 8"

    @property
    def representation(self) -> str:
        return "Knight(Board(9, 9, 3, 3, None, None, None, None), [2, 4, 6, 8])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, ComposedItem, Knight, Cell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
