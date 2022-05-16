import unittest
from typing import Type

from src.items.board import Board
from src.items.exclusion import Exclusion
from src.items.item import Item
from src.utils.coord import Coord
from tests.items.test_item import TestItem


class TestExclusion(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Exclusion(self.board, Coord(2, 2), "12")

    @property
    def clazz(self):
        return Exclusion

    @property
    def representation(self) -> str:
        return "Exclusion(Board(9, 9, 3, 3, None, None, None, None), Coord(2, 2), '12')"

    @property
    def config(self) -> str:
        return "Exclusion: 22=12"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Exclusion}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
