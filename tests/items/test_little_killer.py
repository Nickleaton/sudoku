import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.little_killer import LittleKiller
from src.items.region import Region
from src.utils.cyclic import Cyclic
from src.utils.side import Side
from tests.items.test_region import TestRegion


class TestLittleKiller1(TestRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = LittleKiller(self.board, Side.TOP, Cyclic.CLOCKWISE, 3, 20)
        self.size = 6

    @property
    def clazz(self):
        return LittleKiller

    @property
    def representation(self) -> str:
        return "LittleKiller(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, Cyclic.CLOCKWISE, 3, 20)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, ComposedItem, Item, LittleKiller, Region}

    @property
    def config(self) -> str:
        return "LittleKiller: T3C=20"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def inside(self) -> Cell:
        return Cell.make(self.board, 1, 4)


class TestLittleKiller2(TestRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = LittleKiller(self.board, Side.RIGHT, Cyclic.CLOCKWISE, 3, 20)
        self.size = 6

    @property
    def clazz(self):
        return LittleKiller

    @property
    def representation(self) -> str:
        return "LittleKiller(Board(9, 9, 3, 3, None, None, None, None), Side.RIGHT, Cyclic.CLOCKWISE, 3, 20)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, ComposedItem, Item, LittleKiller, Region}

    @property
    def config(self) -> str:
        return "LittleKiller: R3C=20"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def inside(self) -> Cell:
        return Cell.make(self.board, 9, 4)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
