"""TestQuadrupleBase module."""

import unittest
from typing import Type

from postponed.src.items.quadruple_base import QuadrupleBase
from src.items.item import Item
from src.utils.coord import Coord
from tests.items.test_item import TestItem


class TestQuadrupleBase(TestItem):
    """Test suite for the QuadrupleBase class."""

    def setUp(self) -> None:
        """Set up start_location test instance of QuadrupleBase."""
        super().setUp()
        self.item = QuadrupleBase(self.board, Coord(2, 2), "12")

    @property
    def clazz(self):
        """Return the QuadrupleBase class."""
        return QuadrupleBase

    @property
    def representation(self) -> str:
        """Return the string representation of QuadrupleBase."""
        return "QuadrupleBase(Board(9, 9, {}), Coord(2, 2), '12')"

    @property
    def config(self) -> str:
        """Return the configuration string for QuadrupleBase."""
        return "QuadrupleBase: 22=12"

    @property
    def has_rule(self) -> bool:
        """Return whether the QuadrupleBase has an associated rule."""
        return False

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the QuadrupleBase instance should belong to."""
        return {Item, QuadrupleBase}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
