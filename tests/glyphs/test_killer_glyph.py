import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.killer_glyph import KillerGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestKillerGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        cells = [
            Coord(1, 3),
            Coord(2, 3),
            Coord(3, 1),
            Coord(3, 2),
            Coord(3, 3),
            Coord(4, 2),
            Coord(4, 3),
            Coord(4, 4),
            Coord(5, 4)
        ]
        self.glyph = KillerGlyph('Style', cells)

    @property
    def target(self):
        return (
            '<g>'
            '<line class="Style" x1="300" x2="400" y1="100" y2="100" />'
            '<line class="Style" x1="100" x2="100" y1="300" y2="400" />'
            '<line class="Style" x1="300" x2="300" y1="300" y2="100" />'
            '<line class="Style" x1="300" x2="100" y1="300" y2="300" />'
            '<line class="Style" x1="100" x2="200" y1="400" y2="400" />'
            '<line class="Style" x1="200" x2="200" y1="400" y2="500" />'
            '<line class="Style" x1="400" x2="400" y1="400" y2="100" />'
            '<line class="Style" x1="400" x2="500" y1="400" y2="400" />'
            '<line class="Style" x1="400" x2="200" y1="500" y2="500" />'
            '<line class="Style" x1="400" x2="400" y1="500" y2="600" />'
            '<line class="Style" x1="400" x2="500" y1="600" y2="600" />'
            '<line class="Style" x1="500" x2="500" y1="600" y2="400" />'
            '</g>'
        )

    @property
    def representation(self) -> str:
        return (
            "KillerGlyph('Style', "
            "["
            "Coord(1, 3), Coord(2, 3), Coord(3, 1), Coord(3, 2), Coord(3, 3), "
            "Coord(4, 2), Coord(4, 3), Coord(4, 4), Coord(5, 4)"
            "]"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, KillerGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
