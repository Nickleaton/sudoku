import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.quadruple_glyph import QuadrupleGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestQuadrupleGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = QuadrupleGlyph("Style", Coord(2, 2), "1234")

    @property
    def target(self):
        return (
            '<g>'
            '<circle class="StyleCircle" cx="300" cy="300" r="35" />'
            '<text class="StyleText" transform="translate(300, 300)">'
            '<tspan alignment-baseline="central" text-anchor="middle">1234</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return "QuadrupleGlyph('Style', Coord(2, 2), '1234')"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, QuadrupleGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
