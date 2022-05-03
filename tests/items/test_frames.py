import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.first_n import FirstN
from src.items.frame import Frame
from src.items.frames import Frames
from src.items.item import Item
from src.items.region import Region
from src.utils.side import Side
from tests.items.test_composed import TestComposed


class TestFrames(TestComposed):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Frames(
            self.board,
            [
                Frame(self.board, Side.TOP, 1, 10),
                Frame(self.board, Side.LEFT, 1, 11),
                Frame(self.board, Side.BOTTOM, 1, 12),
                Frame(self.board, Side.RIGHT, 1, 13)
            ]
        )
        self.size = 4

    @property
    def clazz(self):
        return Frames

    @property
    def config(self) -> str:
        return "Frames: [ T1=10, L1=11, B1=12, R1=13 ]"

    @property
    def representation(self) -> str:
        return (
            "Frames"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "["
            "Frame(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, 10), "
            "Frame(Board(9, 9, 3, 3, None, None, None, None), Side.LEFT, 11), "
            "Frame(Board(9, 9, 3, 3, None, None, None, None), Side.BOTTOM, 12), "
            "Frame(Board(9, 9, 3, 3, None, None, None, None), Side.RIGHT, 13)"
            "]"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, FirstN, Item, Region, Frame, Frames}

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
