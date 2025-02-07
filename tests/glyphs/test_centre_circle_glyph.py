"""TestCentreCircleGlyph."""
import unittest

from src.glyphs.centre_circle_glyph import CentreCircleGlyph
from src.glyphs.circle_glyph import CircleGlyph
from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.coord import Coord
from tests.glyphs.test_circle_glyph import TestCircleGlyph

config: Config = Config()


class TestCentreCircleGlyph(TestCircleGlyph):
    """Test suite for the CentreCircleGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for CentreCircleGlyph.

        Initializes an instance of CentreCircleGlyph with the given style, coordinates, and radius.
        """
        super().setUp()
        self.glyph = CentreCircleGlyph('Style', Coord(1, 1), 0.5)

    @property
    def target(self) -> str:
        """Get the target SVG markup for CentreCircleGlyph.

        Returns:
            str: The SVG markup for the circle representing the CentreCircleGlyph.
        """
        return '<circle class="Style" cx="0" cy="0" r="50.0" transform="translate(150.0, 150.0)"/>'

    @property
    def representation(self) -> str:
        """Return the string representation of CentreCircleGlyph.

        Returns:
            str: The string representation of the CentreCircleGlyph instance.
        """
        return "CentreCircleGlyph('Style', 0.5)"

    @property
    def expected_classes(self) -> set[type[Glyph]]:
        """Get the expected set of classes that CentreCircleGlyph should inherit from.

        Returns:
            set[type[Glyph]]: A set containing the expected classes.
        """
        return {CentreCircleGlyph, CircleGlyph, Glyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
