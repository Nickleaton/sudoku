"""TestLockOutLine."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.line import Line
from src.items.lock_out_line import LockOutLine
from src.items.region import Region
from tests.items.test_line import TestLine


class TestLockOutLine(TestLine):
    """Test suite for the LockOutLine class."""

    @property
    def clazz(self):
        """Return the LockOutLine class."""
        return LockOutLine

    @property
    def config(self) -> str:
        """Return the configuration string for the LockOutLine instance."""
        return "LockOutLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        """Return whether the LockOutLine instance has a rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the LockOutLine instance should belong to."""
        return {Cell, ComposedItem, Item, Line, LockOutLine, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
