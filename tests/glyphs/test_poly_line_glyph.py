import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestPolyLineGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = PolyLineGlyph("Style", [Coord(0, 0), Coord(1, 2), Coord(2, 3)], False, False)

    @property
    def target(self):
        return '<polyline class="Style" points="50.0,50.0 250.0,150.0 350.0,250.0" />'

    @property
    def representation(self) -> str:
        return "PolyLineGlyph('Style', [Coord(0, 0), Coord(1, 2), Coord(2, 3)], False, False)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, PolyLineGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
