import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.little_killer import LittleKiller
from src.items.region import Region
from src.utils.cyclic import Cyclic
from src.utils.side import Side
from tests.items.test_item import TestItem


class TestLittleKiller(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = LittleKiller(self.board, Side.TOP, Cyclic.CLOCKWISE, 3, 20)

    @property
    def clazz(self):
        return LittleKiller

    @property
    def representation(self) -> str:
        return "LittleKiller(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, Cyclic.CLOCKWISE, 3, 20)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, Item, LittleKiller, Region}

    @property
    def config(self) -> str:
        return "LittleKiller: T3C=20"

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
