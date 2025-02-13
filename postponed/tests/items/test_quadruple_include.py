"""TestQuadrupleInclude module."""

import unittest
from typing import Type

from postponed.src.items.quadruple_base import QuadrupleBase
from postponed.src.items.quadruple_include import QuadrupleInclude
from postponed.tests.items.test_quadruple_base import TestQuadrupleBase
from src.items.item import Item
from src.utils.coord import Coord


class TestQuadrupleInclude(TestQuadrupleBase):
    """Test suite for the QuadrupleInclude class."""

    def setUp(self) -> None:
        """Set up start_location test instance of QuadrupleInclude."""
        super().setUp()
        self.item = QuadrupleInclude(self.board, Coord(2, 2), "12")

    @property
    def clazz(self):
        """Return the QuadrupleInclude class."""
        return QuadrupleInclude

    @property
    def representation(self) -> str:
        """Return the string representation of QuadrupleInclude."""
        return "QuadrupleInclude(Board(9, 9, {}), Coord(2, 2), '12')"

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
