import unittest
from typing import Type


from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.frozen_thermometer_line import FrozenThermometerLine
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from src.items.thermometer_line import ThermometerLine
from tests.items.test_thermometer import TestThermometerLine


class TestFrozenThermometer(TestThermometerLine):

    @property
    def clazz(self):
        return FrozenThermometerLine

    @property
    def config(self) -> str:
        return "FrozenThermometer: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, ComposedItem, FrozenThermometerLine, Item, Line, Region, ThermometerLine}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
