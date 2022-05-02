import unittest
from typing import Type, Sequence, Tuple, Any

import oyaml as yaml

from src.items.board import Board
from src.items.cell import Cell
from src.items.column_indexer import ColumnIndexer
from src.items.composed import Composed
from src.items.indexing import Indexer
from src.items.item import Item
from src.items.region import Region
from src.items.standard_region import StandardRegion
from tests.items.test_indexer import TestIndexer


class TestColumnIndexer(TestIndexer):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)
        self.item = ColumnIndexer(self.board, 1)

    @property
    def representation(self) -> str:
        return "ColumnIndexer(Board(9, 9, 3, 3, None, None, None, None), 1)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, ColumnIndexer, Composed, Indexer, Item, Region, StandardRegion}

    @property
    def config(self) -> str:
        return "ColumnIndexer: 1"

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.item.__class__.__name__, self.board, data['ColumnIndexer'])
        self.assertIsNotNone(item)

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
