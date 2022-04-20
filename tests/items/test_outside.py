import unittest
from typing import Type, Sequence, Tuple, Any

import oyaml as yaml

from src.items.board import Board
from src.items.item import Item
from src.items.outside import Outside
from src.utils.side import Side
from tests.items.test_item import TestItem


class TestOutside(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Outside(self.board, Side.TOP, 1, [1, 2, 3])

    @property
    def representation(self) -> str:
        return "Outside(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, 1, [1, 2, 3])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Outside}

    @property
    def config(self) -> str:
        return "T1=123"

    @property
    def valid_test_cases(self) -> Sequence[Tuple[Any, Sequence[str]]]:
        return [
            ("T2=123", []),
            ('T0=123', ['Index outside range 0']),
            ('T1=0', ['Not a valid digit 0']),
            (999, ['Expected str, got 999']),
            ('abcd', ['Side not valid a', 'Index not valid b']),
            ('X1=123', ['Side not valid X']),
            ('TX=123', ['Index not valid X']),
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
