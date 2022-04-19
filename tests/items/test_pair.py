import unittest
from typing import Type, Sequence, Tuple, Any

import oyaml as yaml

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.pair import Pair
from tests.items.test_item import TestItem


class TestPair(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Pair(self.board, Cell(None, 1, 2), Cell(None, 1, 3))

    @property
    def representation(self) -> str:
        return "Pair(Board(9, 9, 3, 3, None, None, None, None), Cell(None, 1, 2), Cell(None, 1, 3))"

    @property
    def valid_test_cases(self) -> Sequence[Tuple[Any, Sequence[str]]]:
        return [
            ([[1, 2], [1, 3]], []),
            (1, ['Expecting list, got 1']),
            ([[1, 2]], ['Expecting two cells, got [[1, 2]]']),
            ([[1, 2], ['a', 1]], ['row not int']),
            ([[1, 2], [1, 'b']], ['column not int']),
            ([[1, 2], [1, 'b']], ['column not int']),
            ([[1, 2, 3], [1, 2]], ['expecting row, column']),
            ([[1, 2], [1, 2, 3]], ['expecting row, column']),
        ]

    @property
    def config(self) -> str:
        return "[[1, 2], [1, 3]]"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Item, Pair}

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.item.__class__.__name__, self.board, data)
        self.assertIsNotNone(item)
        self.assertEqual(self.item.__class__, item.__class__)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
