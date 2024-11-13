import unittest
from typing import Type

from src.items.board import Board
from src.items.item import Item
from src.items.quadruple_base import QuadrupleBase
from src.items.quadruple_include import QuadrupleInclude
from src.utils.coord import Coord
from tests.items.test_quadruple_base import TestQuadrupleBase


class TestQuadrupleInclude(TestQuadrupleBase):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = QuadrupleInclude(self.board, Coord(2, 2), "12")

    @property
    def clazz(self):
        return QuadrupleInclude

    @property
    def representation(self) -> str:
        return "QuadrupleInclude(Board(9, 9, 3, 3, None, None, None, None), Coord(2, 2), '12')"

    @property
    def config(self) -> str:
        return "QuadrupleInclude: 22=12"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, QuadrupleBase, QuadrupleInclude}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
