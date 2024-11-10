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
        return '<g />'

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
