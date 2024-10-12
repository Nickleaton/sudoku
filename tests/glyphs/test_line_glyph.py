import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.line_glyph import LineGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestLineGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = LineGlyph("Style", Coord(0, 0), Coord(1, 2))

    @property
    def target(self) -> str:
        return '<line class="Style" x1="0" x2="200" y1="0" y2="100" />'

    @property
    def representation(self) -> str:
        return "LineGlyph('Style', Coord(0, 0), Coord(1, 2))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, LineGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
