import unittest
from typing import Type

from src.items.board import Board
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region_sets import RegionSet
from tests.items.test_composed import TestComposed


class TestRegionSet(TestComposed):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = RegionSet(self.board, [])
        self.size = 0

    @property
    def clazz(self):
        return RegionSet

    @property
    def config(self) -> str:
        return "RegionSet:"

    @property
    def representation(self) -> str:
        return "RegionSet(Board(9, 9, 3, 3, None, None, None, None), [])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, ComposedItem, RegionSet}

    @property
    def has_rule(self) -> bool:
        return False


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
