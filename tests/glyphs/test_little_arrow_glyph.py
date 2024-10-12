import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.little_arrow_glyph import LittleArrowGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestLittleArrowGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = LittleArrowGlyph('Style', Coord(1, 1), 1)

    @property
    def target(self):
        return (
            '<text class="Style" transform="translate(140.0, 140.0) rotate(315.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">▲</tspan>'
            '</text>'
        )

    @property
    def representation(self) -> str:
        return "LittleArrowGlyph('Style', Coord(1, 1), 1)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, LittleArrowGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
