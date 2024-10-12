import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestRectangleGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = RectangleGlyph('Style', Coord(1, 1), Coord(1, 2), 0.25, 2, True)

    @property
    def target(self):
        return (
            '<rect class="Style" height="25.0" transform="translate(150.0, 100.0)" '
            'width="50.0" x="0" y="0" />'
        )

    @property
    def representation(self) -> str:
        return "RectangleGlyph('Style', Coord(1, 1), Coord(1, 2), 0.25, 2, True)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, RectangleGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
