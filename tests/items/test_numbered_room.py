"""TestNumberedRoom."""
import unittest
from pathlib import Path
from typing import Type

from src.items.item import Item
from src.items.numbered_room import NumberedRoom
from src.solvers.pulp_solver import PulpSolver
from src.utils.side import Side
from tests.items.test_item import TestItem


class TestNumberedRoom(TestItem):
    """Test suite for the NumberedRoom class."""

    def setUp(self) -> None:
        """Set up the test environment for NumberedRoom."""
        super().setUp()
        self.item = NumberedRoom(self.board, Side.top, 1, 9)

    @property
    def clazz(self):
        """Return the NumberedRoom class."""
        return NumberedRoom

    @property
    def representation(self) -> str:
        """Return the string representation of the NumberedRoom instance."""
        return "NumberedRoom(Board(9, 9, 3, 3, None), Side.top, 1, 9)"

    @property
    def config(self) -> str:
        """Return the configuration string for NumberedRoom."""
        return "NumberedRoom: T1=9"

    @property
    def has_rule(self) -> bool:
        """Return whether the NumberedRoom instance has start rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the NumberedRoom instance should belong to."""
        return {Item, NumberedRoom}

    def test_add_constraint(self) -> None:
        """Test adding start constraint to the NumberedRoom instance."""
        numbered_rooms = [
            NumberedRoom(self.board, Side.top, 1, 9),
            NumberedRoom(self.board, Side.right, 1, 9),
            NumberedRoom(self.board, Side.bottom, 1, 9),
            NumberedRoom(self.board, Side.left, 1, 9)
        ]
        for room in numbered_rooms:
            log_path = Path("output\\logs\\tests")
            solver = PulpSolver(self.board, 'test', log_path.name)
            room.add_constraint(solver)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
