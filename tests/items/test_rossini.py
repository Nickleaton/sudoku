import unittest
from typing import Type

import oyaml as yaml

from src.items.board import Board
from src.items.composed import Composed
from src.items.item import Item
from src.items.rossini import Rossini, Rossinis
from src.utils.order import Order
from src.utils.side import Side
from tests.items.test_composed import TestComposed
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
    def config(self):
        return "T1I"

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.item.__class__.__name__, self.board, data)
        self.assertIsNotNone(item)
        self.assertEqual(self.item.__class__, item.__class__)

    @property
    def has_rule(self) -> bool:
        return True


class TestRossinis(TestComposed):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Rossinis(
            self.board,
            [
                Rossini(self.board, Side.TOP, 1, Order.INCREASING),
                Rossini(self.board, Side.LEFT, 1, Order.INCREASING),
                Rossini(self.board, Side.BOTTOM, 1, Order.DECREASING),
                Rossini(self.board, Side.RIGHT, 1, Order.DECREASING)
            ]
        )
        self.size = 4

    @property
    def config(self) -> str:
        return "Rossinis: [ T1I, L1I, B1D, R1D ]"

    @property
    def representation(self) -> str:
        return (
            "Rossinis"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "["
            "Rossini(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, 1, Order.INCREASING), "
            "Rossini(Board(9, 9, 3, 3, None, None, None, None), Side.LEFT, 1, Order.INCREASING), "
            "Rossini(Board(9, 9, 3, 3, None, None, None, None), Side.BOTTOM, 1, Order.DECREASING), "
            "Rossini(Board(9, 9, 3, 3, None, None, None, None), Side.RIGHT, 1, Order.DECREASING)"
            "]"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Rossinis, Rossini}

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
