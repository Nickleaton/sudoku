import unittest
from typing import Type, Sequence, Any, Tuple

from src.items.board import Board
from src.items.item import Item
from src.items.quadruple import Quadruple
from src.utils.coord import Coord
from tests.items.test_item import TestItem


class TestQuadruple(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Quadruple(self.board, Coord(2, 2), "12")

    @property
    def representation(self) -> str:
        return "Quadruple(Board(9, 9, 3, 3, None, None, None, None), Coord(2, 2), '12')"

    @property
    def config(self) -> str:
        return "Quadruple: 22=12"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Quadruple}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
