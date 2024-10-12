import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import RectGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestRectGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = RectGlyph('Style', Coord(1, 1), Coord(1, 2))

    @property
    def target(self):
        return '<rect class="Style" height="100" transform="translate(100, 100)" width="200" x="0" y="0" />'

    @property
    def representation(self) -> str:
        return "RectGlyph('Style', Coord(1, 1), Coord(1, 2))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, RectGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
