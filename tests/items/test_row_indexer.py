import unittest
from typing import Type, Sequence, Tuple, Any

import oyaml as yaml

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.indexing import Indexer
from src.items.item import Item
from src.items.region import Region
from src.items.row_indexer import RowIndexer
from src.items.standard_region import StandardRegion
from tests.items.test_indexer import TestIndexer


class TestRowIndexer(TestIndexer):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)
        self.item = RowIndexer(self.board, 1)

    @property
    def representation(self) -> str:
        return "RowIndexer(Board(9, 9, 3, 3, None, None, None, None), 1)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, RowIndexer, Composed, Indexer, Item, Region, StandardRegion}

    @property
    def config(self) -> str:
        return "RowIndexer: 1"

    @property
    def valid_test_cases(self) -> Sequence[Tuple[Any, Sequence[str]]]:
        return [
            ({'RowIndexer': 1}, []),
            ({'RowIndexer': 99}, ["Expecting RowIndexer: index, got {'RowIndexer': 99}"]),
            ({'RowIndexer': None}, ["Expecting RowIndexer: index, got {'RowIndexer': None}"]),
            ({'XXXX': 1}, ["Expecting RowIndexer: index, got {'XXXX': 1}"]),
            ('xxx', ["Expecting RowIndexer: index, got 'xxx'"]),
            ({'RowIndexer': 1, 'Other': None}, ["Expecting RowIndexer: index, got {'RowIndexer': 1, 'Other': None}"])
        ]

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.item.__class__.__name__, self.board, data['RowIndexer'])
        self.assertIsNotNone(item)

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
