"""TestSequenceLine module."""

import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from src.items.sequence_line import SequenceLine
from tests.items.test_line import TestLine


class TestSequenceLine(TestLine):
    """Test suite for the SequenceLine class."""

    @property
    def clazz(self):
        """Return the SequenceLine class."""
        return SequenceLine

    @property
    def config(self) -> str:
        """Return the configuration string for SequenceLine."""
        return "SequenceLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        """Return whether SequenceLine has a rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for SequenceLine."""
        return {Cell, ComposedItem, Item, Line, Region, SequenceLine}

    def test_max_difference(self):
        """Test the max_difference method of the SequenceLine class."""
        self.assertEqual(9, SequenceLine.max_difference(1))
        self.assertEqual(8, SequenceLine.max_difference(2))
        self.assertEqual(3, SequenceLine.max_difference(3))
        self.assertEqual(2, SequenceLine.max_difference(4))
        self.assertEqual(2, SequenceLine.max_difference(5))
        self.assertEqual(1, SequenceLine.max_difference(6))
        self.assertEqual(1, SequenceLine.max_difference(7))
        self.assertEqual(1, SequenceLine.max_difference(8))
        self.assertEqual(1, SequenceLine.max_difference(9))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
