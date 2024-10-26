import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import SquareGlyph, RectGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestSquareGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = SquareGlyph('Style', position=Coord(10, 10), size=50)

    @property
    def target(self):
        return '<rect class="Style" height="5000" transform="translate(1000, 1000)" width="5000" x="0" y="0" />'

    @property
    def representation(self) -> str:
        return "SquareGlyph('Style', Coord(10, 10), 50)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, RectGlyph, SquareGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
