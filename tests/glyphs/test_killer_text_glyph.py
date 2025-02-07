"""TestKillerTextGlyph."""
import unittest

from src.glyphs.glyph import Glyph
from src.glyphs.killer_text_glyph import KillerTextGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestKillerTextGlyph(TestGlyph):
    """Test suite for the KillerTextGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for KillerTextGlyph.

        Initializes the style, coordinates, and text for the KillerTextGlyph.
        """
        super().setUp()
        self.glyph = KillerTextGlyph('Style', 0, Coord(1, 1), 'abcd')

    @property
    def target(self):
        """Get the target SVG markup for the KillerTextGlyph.

        Returns:
            str: The expected target SVG markup for the KillerTextGlyph.
        """
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(105.0, 105.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">abcd</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(105.0, 105.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">abcd</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        """Get the string representation of the KillerTextGlyph instance.

        Returns:
            str: The string representation of the KillerTextGlyph.
        """
        return "KillerTextGlyph('Style', 0.0, Coord(1, 1), 'abcd')"

    @property
    def expected_classes(self) -> set[type[Glyph]]:
        """Get the expected set of classes that KillerTextGlyph should inherit from.

        Returns:
            set[type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, KillerTextGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
