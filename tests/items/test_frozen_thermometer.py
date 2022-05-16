import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed import Composed
from src.items.frozen_thermometer import FrozenThermometer
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from src.items.thermometer import Thermometer
from tests.items.test_thermometer import TestThermometer


class TestFrozenThermometer(TestThermometer):

    @property
    def clazz(self):
        return FrozenThermometer

    @property
    def config(self) -> str:
        return "FrozenThermometer: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, FrozenThermometer, Item, Line, Region, Thermometer}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
