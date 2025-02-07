"""TestKropkiGlyph."""
import unittest

from src.glyphs.glyph import Glyph
from src.glyphs.kropki_glyph import KropkiGlyph
from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.coord import Coord
from tests.glyphs.test_circle_glyph import TestCircleGlyph


class TestKropkiGlyph(TestCircleGlyph):
    """Test suite for the KropkiGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for KropkiGlyph.

        Initializes the style, start_location coordinate, and end_location coordinate for the KropkiGlyph.
        """
        super().setUp()
        self.glyph = KropkiGlyph('Style', Coord(1, 1), Coord(2, 1))

    @property
    def target(self):
        """Get the expected SVG markup for the KropkiGlyph.

        Returns:
            str: The expected target SVG markup for the KropkiGlyph.
        """
        return '<rect class="Style" height="25.0" transform="translate(100.0, 150.0)" width="50.0" x="0" y="0" />'

    @property
    def representation(self) -> str:
        """Get the string representation of the KropkiGlyph instance.

        Returns:
            str: The string representation of the KropkiGlyph.
        """
        return "KropkiGlyph('Style', Coord(1, 1), Coord(2, 1))"

    @property
    def expected_classes(self) -> set[type[Glyph]]:
        """Get the expected set of classes that KropkiGlyph should inherit from.

        Returns:
            set[type[Glyph]]: A set containing the expected classes.
        """
        return {RectangleGlyph, Glyph, KropkiGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
