import unittest
from typing import Type

from src.items.board import Board
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.orthogonally_adjacent import OrthogonallyAdjacent
from tests.items.test_composed import TestComposed


class TestOrthogonallyAdjacent(TestComposed):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = OrthogonallyAdjacent(self.board)

    @property
    def size(self):
        return 0

    @property
    def clazz(self):
        return OrthogonallyAdjacent

    @property
    def representation(self) -> str:
        return "OrthogonallyAdjacent(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {OrthogonallyAdjacent, ComposedItem, Item}

    @property
    def config(self) -> str:
        return "OrthogonallyAdjacent:"

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
