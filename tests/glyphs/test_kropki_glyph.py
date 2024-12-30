"""TestKropkiGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.kropki_glyph import KropkiGlyph
from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.coord import Coord
from tests.glyphs.test_circle_glyph import TestCircleGlyph


class TestKropkiGlyph(TestCircleGlyph):
    """Test suite for the KropkiGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for KropkiGlyph.

        Initializes the style, start coordinate, and end coordinate for the KropkiGlyph.
        """
        super().setUp()
        self.glyph = KropkiGlyph('Style', Coord(1, 1), Coord(1, 2))

    @property
    def target(self):
        """Get the expected SVG markup for the KropkiGlyph.

        Returns:
            str: The expected target SVG markup for the KropkiGlyph.
        """
        return '<rect class="Style" height="50.0" transform="translate(150.0, 100.0)" width="25.0" digit1="0" digit2="0" />'

    @property
    def representation(self) -> str:
        """Get the string representation of the KropkiGlyph instance.

        Returns:
            str: The string representation of the KropkiGlyph.
        """
        return "KropkiGlyph('Style', Coord(1, 1), Coord(1, 2))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that KropkiGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {RectangleGlyph, Glyph, KropkiGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
