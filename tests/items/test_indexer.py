import unittest
from typing import Type

from src.items.board import Board
from src.items.composed_item import ComposedItem
from src.items.indexing import Indexer
from src.items.item import Item
from src.items.region import Region
from src.items.standard_region import StandardRegion
from tests.items.test_standard_region import TestStandardRegion


class TestIndexer(TestStandardRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)
        self.item = Indexer(self.board, 1)
        self.size = 0

    @property
    def clazz(self):
        return Indexer

    @property
    def representation(self) -> str:
        return "Indexer(Board(9, 9, 3, 3, None, None, None, None), 1)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, ComposedItem, StandardRegion, Region, Indexer}

    @property
    def config(self) -> str:
        return "Indexer: 1"

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
