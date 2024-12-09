"""TestQuadro module."""

import unittest
from typing import Type

from src.board.board import Board
from src.items.item import Item
from src.items.quadro import Quadro
from tests.items.test_item import TestItem


class TestQuadro(TestItem):
    """Test suite for the Quadro class."""

    def setUp(self) -> None:
        """Set up start test instance of Quadro."""
        super().setUp()

        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Quadro(self.board)

    @property
    def clazz(self):
        """Return the Quadro class."""
        return Quadro

    @property
    def representation(self) -> str:
        """Return the string representation of Quadro."""
        return "Quadro(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def config(self) -> str:
        """Return the configuration string for Quadro."""
        return "Quadro:"

    @property
    def has_rule(self) -> bool:
        """Return whether the Quadro has an associated rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Quadro instance should belong to."""
        return {Item, Quadro}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
