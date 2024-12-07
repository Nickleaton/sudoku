"""TestQuadrupleExclude module."""

import unittest
from typing import Type

from src.items.item import Item
from src.items.quadruple_base import QuadrupleBase
from src.items.quadruple_exclude import QuadrupleExclude
from src.utils.coord import Coord
from tests.items.test_quadruple_base import TestQuadrupleBase


class TestQuadrupleExclude(TestQuadrupleBase):
    """Test suite for the QuadrupleExclude class."""

    def setUp(self) -> None:
        """Set up a test instance of QuadrupleExclude."""
        super().setUp()
        self.item = QuadrupleExclude(self.board, Coord(2, 2), "12")

    @property
    def clazz(self):
        """Return the QuadrupleExclude class."""
        return QuadrupleExclude

    @property
    def representation(self) -> str:
        """Return the string representation of QuadrupleExclude."""
        return "QuadrupleExclude(Board(9, 9, 3, 3, None, None, None, None), Coord(2, 2), '12')"

    @property
    def config(self) -> str:
        """Return the configuration string for QuadrupleExclude."""
        return "QuadrupleExclude: 22=12"

    @property
    def has_rule(self) -> bool:
        """Return whether the QuadrupleExclude has an associated rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the QuadrupleExclude instance should belong to."""
        return {Item, QuadrupleBase, QuadrupleExclude}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
