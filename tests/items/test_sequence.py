import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from src.items.sequence import Sequence
from tests.items.test_line import TestLine


class TestSequence(TestLine):

    @property
    def clazz(self):
        return Sequence

    @property
    def config(self) -> str:
        return "Sequence: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, Item, Line, Region, Sequence}

    def test_max_difference(self):
        self.assertEqual(9, Sequence.max_diffence(1))
        self.assertEqual(8, Sequence.max_diffence(2))
        self.assertEqual(3, Sequence.max_diffence(3))
        self.assertEqual(2, Sequence.max_diffence(4))
        self.assertEqual(2, Sequence.max_diffence(5))
        self.assertEqual(1, Sequence.max_diffence(6))
        self.assertEqual(1, Sequence.max_diffence(7))
        self.assertEqual(1, Sequence.max_diffence(8))
        self.assertEqual(1, Sequence.max_diffence(9))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
