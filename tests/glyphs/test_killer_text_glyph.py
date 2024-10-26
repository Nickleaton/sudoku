import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.killer_text_glyph import KillerTextGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestKillerTextGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = KillerTextGlyph('Style', 0, Coord(1, 1), 'abcd')

    @property
    def target(self):
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(105.0, 105.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">abcd</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(105.0, 105.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">abcd</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return "KillerTextGlyph('Style', 0.0, Coord(1, 1), 'abcd')"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, KillerTextGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
