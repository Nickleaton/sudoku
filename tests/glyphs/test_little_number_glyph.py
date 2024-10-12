import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.little_number_glyph import LittleNumberGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestLittleNumberGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = LittleNumberGlyph('Style', Coord(1, 1), 1)

    @property
    def target(self):
        return (
            '<text class="Style" transform="translate(135.0, 135.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">1</tspan>'
            '</text>'
        )

    @property
    def representation(self) -> str:
        return "LittleNumberGlyph('Style', Coord(1, 1), 1)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, LittleNumberGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
