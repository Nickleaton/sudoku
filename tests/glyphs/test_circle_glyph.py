import unittest
from typing import Type

from src.glyphs.circle_glyph import CircleGlyph
from src.glyphs.glyph import Glyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestCircleGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = CircleGlyph('Style', Coord(1, 1), 0.5)

    @property
    def target(self):
        return '<circle class="Style" cx="0" cy="0" r="50.0" transform="translate(100, 100)" />'

    @property
    def representation(self) -> str:
        return "CircleGlyph('Style', Coord(1, 1), 0.5)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {CircleGlyph, Glyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
