import unittest
from typing import Type

from src.items.board import Board
from src.items.composed import Composed
from src.items.item import Item
from tests.items.test_item import TestItem


class TestComposed(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Composed(self.board, [])
        self.size = 0

    @property
    def clazz(self):
        return Composed

    def test_construction(self):
        self.assertEqual(self.size, len(self.item.items))

    def test_iteration(self):
        count = 0
        for _ in self.item:
            count += 1
        self.assertEqual(self.size, count)

    @property
    def config(self) -> str:
        return "Composed:"

    @property
    def representation(self) -> str:
        return "Composed(Board(9, 9, 3, 3, None, None, None, None), [])"

    @property
    def has_rule(self) -> bool:
        return False

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
