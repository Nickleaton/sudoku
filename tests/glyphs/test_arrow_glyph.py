"""TestArrowGlyph."""
import unittest

from src.glyphs.arrow_glyph import ArrowGlyph
from src.glyphs.glyph import Glyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestArrowGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = ArrowGlyph('Style', 90.0, Coord(0, 0))

    @property
    def start_marker(self) -> str:
        return ""

    @property
    def end_marker(self) -> str:
        return ""

    @property
    def symbol(self) -> str:
        return ""

    @property
    def target(self):
        return (
            '<text class="Style" transform="translate(0.0, 0.0) rotate(90.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">↑</tspan></text>'
        )

    @property
    def representation(self) -> str:
        return "ArrowGlyph('Style', 90.0, Coord(0, 0))"

    @property
    def expected_classes(self) -> set[type[Glyph]]:
        return {ArrowGlyph, Glyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
