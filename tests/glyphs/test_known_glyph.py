import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.known_glyph import KnownGlyph
from src.glyphs.simple_text_glyph import SimpleTextGlyph
from src.glyphs.text_glyph import TextGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestKnownGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = KnownGlyph('Style', Coord(1, 1), 1)

    @property
    def target(self):
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(150.0, 150.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">1</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(150.0, 150.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">1</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return "KnownGlyph('Style', Coord(1, 1), 1)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, KnownGlyph, SimpleTextGlyph, TextGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
