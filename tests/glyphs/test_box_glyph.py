import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import BoxGlyph, RectGlyph
from src.utils.coord import Coord
from tests.glyphs.test_square_glyph import TestSquareGlyph


class TestBoxGlyph(TestSquareGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = BoxGlyph('Style', Coord(1, 1), Coord(3, 3))

    @property
    def target(self):
        return '<rect class="Style" height="300" transform="translate(100, 100)" width="300" x="0" y="0" />'

    @property
    def representation(self) -> str:
        return "BoxGlyph('Style', Coord(1, 1), Coord(3, 3))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {BoxGlyph, Glyph, RectGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
