"""TestSideCircleGlyph."""
import unittest
from typing import Type

from src.glyphs.circle_glyph import CircleGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.side_circle_glyph import SideCircleGlyph
from src.utils.config import Config
from src.utils.coord import Coord
from tests.glyphs.test_circle_glyph import TestCircleGlyph

config: Config = Config()


class TestSideCircleGlyph(TestCircleGlyph):
    """Test suite for the SideCircleGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for SideCircleGlyph.

        Initializes an instance of SideCircleGlyph with the given style, coordinates, and radius.
        """
        super().setUp()
        self.location1 = Coord(1, 1)
        self.location2 = Coord(1, 2)
        self.glyph = SideCircleGlyph('Style', self.location1, self.location2, 0.5)

    @property
    def target(self) -> str:
        """Get the target SVG markup for SideCircleGlyph.

        Returns:
            str: The SVG markup for the circle representing the SideCircleGlyph.
        """
        return '<circle class="Style" cx="0" cy="0" r="50.0" transform="translate(100.0, 150.0)"/>'

    @property
    def representation(self) -> str:
        """Return the string representation of SideCircleGlyph.

        Returns:
            str: The string representation of the SideCircleGlyph instance.
        """
        return 'SideCircleGlyph(\'Style\', Coord(1, 1), Coord(1, 2), 0.5)'

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that SideCircleGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {SideCircleGlyph, CircleGlyph, Glyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
