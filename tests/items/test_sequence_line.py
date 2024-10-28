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

    @property
    def clazz(self):
        return SequenceLine

    @property
    def config(self) -> str:
        return "SequenceLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, ComposedItem, Item, Line, Region, SequenceLine}

    def test_max_difference(self):
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
