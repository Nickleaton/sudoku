import unittest
from typing import Type

from src.items.board import Board
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.special_region import SpecialRegion
from tests.items.test_region import TestRegion


class TestSpecialRegion(TestRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = SpecialRegion(self.board)
        self.size = 0

    @property
    def clazz(self):
        return SpecialRegion

    @property
    def config(self) -> str:
        return "SpecialRegion:"

    @property
    def representation(self) -> str:
        return "SpecialRegion(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, ComposedItem, Region, SpecialRegion}

    def test_in(self):
        self.assertListEqual([], self.item.cells)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
