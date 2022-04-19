import unittest
from typing import Type, Sequence, Tuple, Any

import oyaml as yaml

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.diagonals import Diagonal
from src.items.item import Item
from src.items.region import Region
from tests.items.test_region import TestRegion


class TestDiagonal(TestRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)
        self.item = Diagonal(self.board)

    @property
    def representation(self) -> str:
        return "Diagonal(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Region, Diagonal}

    @property
    def config(self) -> str:
        return "Diagonal: 1"

    @property
    def valid_test_cases(self) -> Sequence[Tuple[Any, Sequence[str]]]:
        return [
            ({'Diagonal': None}, []),
            ({'Diagonal': 1}, ["Expecting Diagonal with no values, got {'Diagonal': 1}"]),
            ('xxx', ["Expecting a dict got, 'xxx'"]),
            ({'Diagonal': None, 'Other': None},
             [
                 "Expecting one item got, {'Diagonal': None, 'Other': None}",
                 "Expecting Diagonal, got {'Diagonal': None, 'Other': None}"
             ]
             )
        ]

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.item.__class__.__name__, self.board, data)
        self.assertIsNotNone(item)

    @property
    def has_rule(self) -> bool:
        return True

    def test_in(self):
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
