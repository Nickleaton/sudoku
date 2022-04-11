import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed import Composed
from src.items.dutch_whisper import DutchWhisper
from src.items.item import Item
from src.items.line import Line, DifferenceLine
from src.items.region import Region
from tests.items.test_line import TestDifferenceLine


class TestDutchWhispers(TestDifferenceLine):

    @property
    def clazz(self):
        return DutchWhisper

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, DifferenceLine, DutchWhisper, Item, Line, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
