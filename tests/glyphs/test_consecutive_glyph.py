import unittest
from typing import Type

from src.glyphs.consecutive_glyph import ConsecutiveGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.coord import Coord
from tests.glyphs.test_circle_glyph import TestCircleGlyph


class TestConsecutiveGlyph(TestCircleGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = ConsecutiveGlyph('Style', Coord(1, 1), Coord(1, 2))

    @property
    def target(self):
        return '<rect class="Style" height="50.0" transform="translate(150.0, 100.0)" width="25.0" x="0" y="0" />'

    @property
    def representation(self) -> str:
        return "ConsecutiveGlyph('Style', Coord(1, 1), Coord(1, 2))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {RectangleGlyph, ConsecutiveGlyph, Glyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
