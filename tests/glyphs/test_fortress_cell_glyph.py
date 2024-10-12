import unittest
from typing import Type

from src.glyphs.fortress_cell_glyph import FortressCellGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import RectGlyph, SquareGlyph
from src.utils.coord import Coord
from tests.glyphs.test_square_glyph import TestSquareGlyph


class TestFortressCellGlyph(TestSquareGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = FortressCellGlyph('Style', Coord(1, 1))

    @property
    def target(self):
        return (
            '<rect class="Style" height="100" '
            'transform="translate(100, 100)" width="100" x="0" y="0" />'
        )

    @property
    def representation(self) -> str:
        return "FortressCellGlyph('Style', Coord(1, 1))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {FortressCellGlyph, Glyph, RectGlyph, SquareGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
