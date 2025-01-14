"""TestKillerGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.killer_glyph import KillerGlyph
from src.utils.point import Point
from tests.glyphs.test_glyph import TestGlyph


class TestKillerGlyph(TestGlyph):
    """Test suite for the KillerGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for KillerGlyph.

        Initializes the cells and start KillerGlyph instance for testing.
        """
        super().setUp()
        cells = [
            Point(1, 3),
            Point(2, 3),
            Point(3, 1),
            Point(3, 2),
            Point(3, 3),
            Point(4, 2),
            Point(4, 3),
            Point(4, 4),
            Point(5, 4)
        ]
        self.glyph = KillerGlyph('Style', cells)

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
            "Point(1, 3), Point(2, 3), Point(3, 1), Point(3, 2), Point(3, 3), "
            "Point(4, 2), Point(4, 3), Point(4, 4), Point(5, 4)"
            "]"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that KillerGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, KillerGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
