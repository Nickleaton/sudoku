import unittest
from typing import Type

from src.glyphs.edge_text_glyph import EdgeTextGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestEdgeTextGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = EdgeTextGlyph('Style', 0, Coord(1, 1), Coord(1, 2), 'X')

    @property
    def target(self):
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(150.0, 100.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">X</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(150.0, 100.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">X</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return "EdgeTextGlyph('Style', 0.0, Coord(1, 1), Coord(1, 2), 'X')"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {EdgeTextGlyph, Glyph, TextGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
