import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestTextGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = TextGlyph('Style', 90, Coord(10, 10), "abcd")

    @property
    def target(self):
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(1000, 1000) rotate(90.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">abcd</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(1000, 1000) rotate(90.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">abcd</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return "TextGlyph('Style', 90.0, Coord(10, 10), 'abcd')"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, TextGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
