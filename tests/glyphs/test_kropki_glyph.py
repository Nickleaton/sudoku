import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.kropki_glyph import KropkiGlyph
from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.coord import Coord
from tests.glyphs.test_circle_glyph import TestCircleGlyph


class TestKropkiGlyph(TestCircleGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = KropkiGlyph('Style', Coord(1, 1), Coord(1, 2))

    @property
    def target(self):
        return '<rect class="Style" height="50.0" transform="translate(150.0, 100.0)" width="25.0" x="0" y="0" />'

    @property
    def representation(self) -> str:
        return "KropkiGlyph('Style', Coord(1, 1), Coord(1, 2))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {RectangleGlyph, Glyph, KropkiGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
