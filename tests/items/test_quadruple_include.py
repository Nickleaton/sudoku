"""TestQuadrupleInclude module."""

import unittest
from typing import Type

from src.items.board import Board
from src.items.item import Item
from src.items.quadruple_base import QuadrupleBase
from src.items.quadruple_include import QuadrupleInclude
from src.utils.coord import Coord
from tests.items.test_quadruple_base import TestQuadrupleBase


class TestQuadrupleInclude(TestQuadrupleBase):
    """Test suite for the QuadrupleInclude class."""

    def setUp(self) -> None:
        """Set up a test instance of QuadrupleInclude."""
        super().setUp()
        self.item = QuadrupleInclude(self.board, Coord(2, 2), "12")

    @property
    def clazz(self):
        """Return the QuadrupleInclude class."""
        return QuadrupleInclude

    @property
    def representation(self) -> str:
        """Return the string representation of QuadrupleInclude."""
        return "QuadrupleInclude(Board(9, 9, 3, 3, None, None, None, None), Coord(2, 2), '12')"

    @property
    def config(self) -> str:
        """Return the configuration string for QuadrupleInclude."""
        return "QuadrupleInclude: 22=12"

    @property
    def has_rule(self) -> bool:
        """Return whether the QuadrupleInclude has an associated rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the QuadrupleInclude instance should belong to."""
        return {Item, QuadrupleBase, QuadrupleInclude}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
