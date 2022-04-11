import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed import Composed
from src.items.german_whisper import GermanWhisper
from src.items.item import Item
from src.items.line import Line, DifferenceLine
from src.items.region import Region
from tests.items.test_line import TestDifferenceLine


class TestGermanWhisper(TestDifferenceLine):

    @property
    def clazz(self):
        return GermanWhisper

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, DifferenceLine, GermanWhisper, Item, Line, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
