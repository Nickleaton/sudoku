"""TestPalindromeLine."""
import unittest
from typing import Type

from postponed.src.items.line import Line
from postponed.src.items.palindrome_line import PalindromeLine
from postponed.tests.items.test_line import TestLine
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestPalindromeLine(TestLine):
    """Test suite for the PalindromeLine class."""

    @property
    def clazz(self):
        """Return the PalindromeLine class."""
        return PalindromeLine

    @property
    def config(self) -> str:
        """Return the configuration string for PalindromeLine."""
        return "PalindromeLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        """Return whether PalindromeLine has an associated rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the PalindromeLine instance should belong to."""
        return {Cell, ComposedItem, Item, Line, PalindromeLine, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
