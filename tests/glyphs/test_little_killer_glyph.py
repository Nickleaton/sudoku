import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.little_killer_glyph import LittleKillerGlyph
from src.utils.coord import Coord
from src.utils.direction import Direction
from tests.glyphs.test_glyph import TestGlyph


class TestLittleKillerGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = LittleKillerGlyph('Style', Coord(0, 0), Direction.DOWN_RIGHT.angle, 20)

    @property
    def target(self):
        return (
            '<g>'
            '<text class="Style" transform="translate(50.0, 50.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">20</tspan>'
            '</text>'
            '<text class="Style" transform="translate(50.0, 50.0) rotate(135.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">ꜛ</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return "LittleKillerGlyph('Style', Coord(0, 0), Angle(135.0), 20)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, LittleKillerGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
