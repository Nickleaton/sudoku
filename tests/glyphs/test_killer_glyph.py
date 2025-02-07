"""TestKillerGlyph."""
import unittest

from src.glyphs.glyph import Glyph
from src.glyphs.killer_glyph import KillerGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestKillerGlyph(TestGlyph):
    """Test suite for the KillerGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for KillerGlyph.

        Initializes the cells and start_location KillerGlyph instance for testing.
        """
        super().setUp()
        cells = (
            Coord(1, 3),
            Coord(2, 3),
            Coord(3, 1),
            Coord(3, 2),
            Coord(3, 3),
            Coord(4, 2),
            Coord(4, 3),
            Coord(4, 4),
            Coord(5, 4)
        )
        self.glyph = KillerGlyph('Style', list(cells))

    @property
    def target(self):
        """Get the target SVG markup for the KillerGlyph.

        Returns:
            str: The expected target SVG markup.
        """
        return '<g />'

    @property
    def representation(self) -> str:
        """Get the string representation of the KillerGlyph instance.

        Returns:
            str: The string representation of the KillerGlyph.
        """
        return (
            "KillerGlyph('Style', "
            "["
            "Coord(1, 3), Coord(2, 3), Coord(3, 1), Coord(3, 2), Coord(3, 3), "
            "Coord(4, 2), Coord(4, 3), Coord(4, 4), Coord(5, 4)"
            "]"
            ")"
        )

    @property
    def expected_classes(self) -> set[type[Glyph]]:
        """Get the expected set of classes that KillerGlyph should inherit from.

        Returns:
            set[type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, KillerGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
