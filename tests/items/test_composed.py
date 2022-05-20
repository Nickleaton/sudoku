import unittest
from typing import Type

from src.items.board import Board
from src.items.composed_item import ComposedItem
from src.items.item import Item
from tests.items.test_item import TestItem


class TestComposed(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = ComposedItem(self.board, [])
        self.size = 0

    @property
    def clazz(self):
        return ComposedItem

    def test_construction(self):
        self.assertEqual(self.size, len(self.item.items))

    def test_iteration(self):
        count = 0
        for _ in self.item:
            count += 1
        self.assertEqual(self.size, count)

    @property
    def config(self) -> str:
        return "ComposedItem:"

    @property
    def representation(self) -> str:
        return "ComposedItem(Board(9, 9, 3, 3, None, None, None, None), [])"

    @property
    def has_rule(self) -> bool:
        return False

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, ComposedItem}

    def test_top(self):
        child = Item(self.board)
        self.item.add(child)
        self.assertEqual(self.item, self.item.top)
        self.assertEqual(self.item, child.top)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
