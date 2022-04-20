import unittest
from typing import Type

from src.items.board import Board
from src.items.composed import Composed
from src.items.item import Item
from src.items.rossini import Rossini
from src.items.rossinis import Rossinis
from src.utils.order import Order
from src.utils.side import Side
from tests.items.test_composed import TestComposed


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