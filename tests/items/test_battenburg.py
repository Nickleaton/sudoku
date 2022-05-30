import unittest
from typing import Type

from src.items.battenburg import Battenburg
from src.items.board import Board
from src.items.item import Item
from src.utils.coord import Coord
from tests.items.test_item import TestItem


class TestBattenburg(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Battenburg(self.board, Coord(2, 2))

    @property
    def clazz(self):
        return Battenburg

    @property
    def representation(self) -> str:
        return "Battenburg(Board(9, 9, 3, 3, None, None, None, None), Coord(2, 2))"

    @property
    def config(self) -> str:
        return "Battenburg: 22"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Battenburg}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
