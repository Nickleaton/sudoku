import unittest
from typing import Type

from src.items.board import Board
from src.items.composed import Composed
from src.items.item import Item
from src.items.outside import Outside
from src.items.outsides import Outsides
from src.utils.side import Side
from tests.items.test_composed import TestComposed


class TestOutsides(TestComposed):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Outsides(
            self.board,
            [
                Outside(self.board, Side.TOP, 1, [1, 2]),
                Outside(self.board, Side.LEFT, 1, [1, 2]),
                Outside(self.board, Side.BOTTOM, 1, [1, 2]),
                Outside(self.board, Side.RIGHT, 1, [1, 2])
            ]
        )
        self.size = 4

    @property
    def config(self) -> str:
        return "Outsides: [ T1=12, L1=12, B1=12, R1=12 ]"

    @property
    def representation(self) -> str:
        return (
            "Outsides"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "["
            "Outside(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, 1, [1, 2]), "
            "Outside(Board(9, 9, 3, 3, None, None, None, None), Side.LEFT, 1, [1, 2]), "
            "Outside(Board(9, 9, 3, 3, None, None, None, None), Side.BOTTOM, 1, [1, 2]), "
            "Outside(Board(9, 9, 3, 3, None, None, None, None), Side.RIGHT, 1, [1, 2])"
            "]"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Outsides, Outside}

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
