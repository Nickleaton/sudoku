import unittest
from typing import Type, Sequence, Any, Tuple

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.first_n import FirstN
from src.items.frame import Frame
from src.items.item import Item
from src.items.region import Region
from src.utils.side import Side
from tests.items.test_first_n import TestFirstN


class TestFrame(TestFirstN):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Frame(self.board, Side.TOP, 1, 20)
        self.size = 9

    @property
    def representation(self) -> str:
        return "Frame(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, 20)"

    @property
    def config(self) -> str:
        return "Frame: T1=20"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, FirstN, Frame, Item, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
