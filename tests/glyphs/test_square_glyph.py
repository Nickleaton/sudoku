import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import SquareGlyph, RectGlyph
from src.utils.point import Point
from tests.glyphs.test_glyph import TestGlyph


class TestSquareGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = SquareGlyph('Style', position=Point(100, 100), size=50)

    @property
    def target(self):
        return '<rect class="Style" height="5000" transform="translate(100, 100)" width="5000" x="0" y="0" />'

    @property
    def representation(self) -> str:
        return "SquareGlyph('Style', Point(100, 100), 50)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, RectGlyph, SquareGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
