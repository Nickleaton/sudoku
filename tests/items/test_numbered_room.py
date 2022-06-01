import unittest
from typing import Type

from src.items.board import Board
from src.items.item import Item
from src.items.numbered_room import NumberedRoom
from src.solvers.pulp_solver import PulpSolver
from src.utils.side import Side
from tests.items.test_item import TestItem


class TestNumberedRoom(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = NumberedRoom(self.board, Side.TOP, 1, 9)

    @property
    def clazz(self):
        return NumberedRoom

    @property
    def representation(self) -> str:
        return "NumberedRoom(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, 1, 9)"

    @property
    def config(self) -> str:
        return "NumberedRoom: T1=9"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, NumberedRoom}

    def test_add_constraint(self) -> None:
        numbered_rooms = [
            NumberedRoom(self.board, Side.TOP, 1, 9),
            NumberedRoom(self.board, Side.RIGHT, 1, 9),
            NumberedRoom(self.board, Side.BOTTOM, 1, 9),
            NumberedRoom(self.board, Side.LEFT, 1, 9)
        ]
        for room in numbered_rooms:
            solver = PulpSolver(self.board, 'test', "output/logs")
            room.add_constraint(solver)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
