import unittest
from typing import Type, Sequence, Any, Tuple

import oyaml as yaml

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.diagonals import Diagonal
from src.items.item import Item
from src.items.region import Region
from src.items.tlbr import TLBR
from tests.items.test_diagonals import TestDiagonal


class TestTLBR(TestDiagonal):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)
        self.item = TLBR(self.board)

    @property
    def representation(self) -> str:
        return "TLBR(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Cell, Region, Diagonal, TLBR}

    @property
    def config(self) -> str:
        return "TLBR:"

    @property
    def valid_test_cases(self) -> Sequence[Tuple[Any, Sequence[str]]]:
        return [
            ({'TLBR': None}, []),
            ({'TLBR': 1}, ["Expecting TLBR with no values, got {'TLBR': 1}"]),
            ('xxx', ["Expecting a dict got, 'xxx'"]),
            ({'TLBR': None, 'Other': None},
             [
                 "Expecting one item got, {'TLBR': None, 'Other': None}",
                 "Expecting TLBR, got {'TLBR': None, 'Other': None}"
             ]
             )
        ]

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.item.__class__.__name__, self.board, data)
        self.assertIsNotNone(item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
