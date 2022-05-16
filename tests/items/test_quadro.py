import unittest
from typing import Type

from src.items.board import Board
from src.items.item import Item
from src.items.quadro import Quadro
from tests.items.test_item import TestItem


class TestQuadro(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Quadro(self.board)

    @property
    def clazz(self):
        return Quadro

    @property
    def representation(self) -> str:
        return "Quadro(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def config(self) -> str:
        return "Quadro:"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Quadro}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
