import unittest
from typing import Type

from src.glyphs.between_line_glyph import BetweenLineGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.coord import Coord
from tests.glyphs.test_poly_line_glyph import TestPolyLineGlyph


class TestBetweenLineGlyph(TestPolyLineGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = BetweenLineGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])

    @property
    def start_marker(self) -> str:
        return (
            '<marker class="Between BetweenStart" id="Between-start" markerHeight="35" markerWidth="35" '
            'refX="50" refY="50" viewBox="0 0 100 100"><circle cx="50" cy="50" r="35" /></marker>'
        )

    @property
    def end_marker(self) -> str:
        return (
            '<marker class="Between BetweenEnd" id="Between-end" markerHeight="35" markerWidth="35" '
            'refX="50" refY="50" viewBox="0 0 100 100"><circle cx="50" cy="50" r="35" /></marker>'
        )

    @property
    def target(self):
        return (
            '<polyline class="Style" '
            'marker-end="url(#Style-end)" '
            'marker-start="url(#Style-start)" '
            'points="150.0,150.0 250.0,150.0 250.0,250.0" />'
        )

    @property
    def representation(self) -> str:
        return "BetweenLineGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {BetweenLineGlyph, Glyph, PolyLineGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
