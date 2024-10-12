import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.odd_cell_glyph import OddCellGlyph
from src.utils.coord import Coord
from tests.glyphs.test_circle_glyph import TestCircleGlyph


class TestOddCellGlyph(TestCircleGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = OddCellGlyph('Style', Coord(1, 1))

    @property
    def symbol(self) -> str:
        return (
            '<symbol class="OddCell" id="OddCell-symbol" viewBox="0 0 100 100">'
            '<circle cx="50" cy="50" r="35" /></symbol>'
        )

    @property
    def target(self):
        return '<use class="OddCell" height="100" width="100" x="100" xlink:href="#OddCell-symbol" y="100" />'

    @property
    def representation(self) -> str:
        return "OddCellGlyph('Style', Coord(1, 1))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, OddCellGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
