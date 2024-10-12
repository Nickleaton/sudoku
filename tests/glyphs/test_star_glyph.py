import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.simple_text_glyph import SimpleTextGlyph
from src.glyphs.star_glyph import StarGlyph
from src.glyphs.text_glyph import TextGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestStarGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = StarGlyph('Style', Coord(1, 1))

    @property
    def target(self):
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(100, 100) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">✧</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(100, 100) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">✧</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return "StarGlyph('Style', Coord(1, 1))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, SimpleTextGlyph, StarGlyph, TextGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
