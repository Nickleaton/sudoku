import unittest
from typing import Type, Sequence, Tuple, Any

import oyaml as yaml

from src.items.board import Board
from src.items.item import Item
from src.items.rossini import Rossini
from src.utils.order import Order
from src.utils.side import Side
from tests.items.test_item import TestItem


class TestRossini(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Rossini(self.board, Side.TOP, 1, Order.INCREASING)

    @property
    def representation(self) -> str:
        return "Rossini(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, 1, Order.INCREASING)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Rossini}

    @property
    def config(self) -> str:
        return "T1I"

    @property
    def valid_test_cases(self) -> Sequence[Tuple[Any, Sequence[str]]]:
        return [
            ("T2I", []),
            (999, ['Expected str, got 999']),
            ('abcd', ["Expected side|index|order, got 'abcd'"]),
            ('X1I', ['Side not valid X']),
            ('TXI', ['Index not valid X']),
            ('T0I', ['Index outside range 0']),
            ('T1X', ['Invalid Order X'])
        ]

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.item.__class__.__name__, self.board, data)
        self.assertIsNotNone(item)
        self.assertEqual(self.item.__class__, item.__class__)

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
