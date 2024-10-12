import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.simple_text_glyph import SimpleTextGlyph
from src.glyphs.text_glyph import TextGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestSimpleTextGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = SimpleTextGlyph('Style', 0, Coord(1, 1), "X")

    @property
    def target(self):
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(100, 100) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">X</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(100, 100) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">X</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return "SimpleTextGlyph('Style', 0.0, Coord(1, 1), 'X')"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, SimpleTextGlyph, TextGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
