"""TestRenbanLine module."""

import unittest
from typing import Type

from postponed.src.items.line import Line
from postponed.src.items.renban_line import RenbanLine
from postponed.tests.items.test_line import TestLine
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestRenbanLine(TestLine):
    """Test suite for the RenbanLine class."""

    @property
    def clazz(self):
        """Return the RenbanLine class."""
        return RenbanLine

    @property
    def config(self) -> str:
        """Return the configuration string for RenbanLine."""
        return "RenbanLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        """Return whether RenbanLine has an associated rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the RenbanLine instance should belong to."""
        return {Cell, ComposedItem, Item, Line, Region, RenbanLine}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
