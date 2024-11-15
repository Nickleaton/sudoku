"""TestBattenburgGlyph."""
import unittest
from typing import Type

from src.glyphs.battenburg_glyph import BattenburgGlyph
from src.glyphs.glyph import Glyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestBattenburgGlyph(TestGlyph):
    """Test suite for BattenburgGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for BattenburgGlyph.

        Initializes an instance of BattenburgGlyph with the given style and coordinates.
        """
        super().setUp()
        self.glyph = BattenburgGlyph('Style', Coord(3, 3))

    @property
    def symbol(self) -> str:
        """Get the SVG symbol for BattenburgGlyph.

        Returns:
            str: The SVG markup for the Battenburg symbol.
        """
        return (
            '<symbol class="Battenberg" id="Battenberg-symbol" viewBox="0 0 100 100">'
            '<rect class="BattenbergPink" height="30.0" transform="translate(0.0, -30.0)" width="30.0" x="0" y="0" />'
            '<rect class="BattenbergYellow" height="30.0" transform="translate(30.0, 0.0)" width="30.0" x="0" y="0" />'
            '<rect class="BattenbergPink" height="30.0" transform="translate(0.0, 30.0)" width="30.0" x="0" y="0" />'
            '<rect class="BattenbergYellow" height="30.0" transform="translate(-30.0, 0.0)" width="30.0" x="0" y="0" />'
            '</symbol>'
        )

    @property
    def target(self):
        """Get the SVG markup for the BattenburgGlyph target.

        Returns:
            str: The SVG markup for the target element using the Battenburg symbol.
        """
        return '<use class="Battenberg" height="100" width="100" x="300" xlink:href="#Battenberg-symbol" y="300" />'

    @property
    def representation(self) -> str:
        """Return the string representation of BattenburgGlyph.

        Returns:
            str: The string representation of the BattenburgGlyph instance.
        """
        return "BattenburgGlyph('Style', Coord(3, 3))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that BattenburgGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {BattenburgGlyph, Glyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
