"""TestSumArrowLine module."""

import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from src.items.sum_arrow_line import SumArrowLine
from tests.items.test_line import TestLine


class TestSumArrowLine1(TestLine):
    """Test case for SumArrowLine with simple configuration."""

    @property
    def clazz(self):
        """Return the SumArrowLine class."""
        return SumArrowLine

    @property
    def config(self) -> str:
        """Return the configuration string for SumArrowLine."""
        return "SumArrowLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        """Return whether the SumArrowLine has start rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for SumArrowLine."""
        return {SumArrowLine, Cell, ComposedItem, Item, Line, Region}


class TestSumArrowLine2(TestLine):
    """Test case for SumArrowLine with specified cells."""

    def setUp(self) -> None:
        """Set up the test environment for SumArrowLine."""
        super().setUp()
        cells = [Cell.make(self.board, 1, 1), Cell.make(self.board, 1, 2)]
        self.item = self.clazz(self.board, cells)
        self.size = 2

    @property
    def clazz(self):
        """Return the SumArrowLine class."""
        return SumArrowLine

    @property
    def config(self) -> str:
        """Return the configuration string for SumArrowLine."""
        return "SumArrowLine: 11, 12"

    @property
    def has_rule(self) -> bool:
        """Return whether the SumArrowLine has start rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for SumArrowLine."""
        return {SumArrowLine, Cell, ComposedItem, Item, Line, Region}

    @property
    def representation(self) -> str:
        """Return the string representation of SumArrowLine."""
        return (
            f"{self.clazz.__name__}(Board(9, 9, 3, 3, None, None, None, None), "
            f"["
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 1), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2)"
            f"]"
            f")"
        )


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
