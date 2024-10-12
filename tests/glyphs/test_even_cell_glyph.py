import unittest
from typing import Type

from src.glyphs.even_cell_glyph import EvenCellGlyph
from src.glyphs.glyph import Glyph
from src.utils.coord import Coord
from tests.glyphs.test_square_glyph import TestSquareGlyph


class TestEvenCellGlyph(TestSquareGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = EvenCellGlyph('Style', Coord(1, 1))

    @property
    def target(self):
        return '<rect class="Style" height="70.0" transform="translate(115.0, 115.0)" width="70.0" x="0" y="0" />'

    @property
    def representation(self) -> str:
        return "EvenCellGlyph('Style', Coord(1, 1))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {EvenCellGlyph, Glyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
