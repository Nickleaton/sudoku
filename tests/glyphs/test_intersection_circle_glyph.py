"""TestIntersectionCircleGlyph."""
import unittest

from src.glyphs.circle_glyph import CircleGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.intersection_circle_glyph import IntersectionCircleGlyph
from src.utils.config import Config
from src.utils.coord import Coord
from tests.glyphs.test_circle_glyph import TestCircleGlyph

config: Config = Config()


class TestIntersectionCircleGlyph(TestCircleGlyph):
    """Test suite for the IntersectionCircleGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for IntersectionCircleGlyph.

        Initializes an instance of IntersectionCircleGlyph with the given style, coordinates, and radius.
        """
        super().setUp()
        self.glyph = IntersectionCircleGlyph('Style', Coord(1, 1), 0.5)

    @property
    def target(self) -> str:
        """Get the target SVG markup for IntersectionCircleGlyph.

        Returns:
            str: The SVG markup for the circle representing the IntersectionCircleGlyph.
        """
        return '<circle class="Style" cx="0" cy="0" r="50.0" transform="translate(200.0, 200.0)"/>'

    @property
    def representation(self) -> str:
        """Return the string representation of IntersectionCircleGlyph.

        Returns:
            str: The string representation of the IntersectionCircleGlyph instance.
        """
        return "IntersectionCircleGlyph('Style', 0.5)"

    @property
    def expected_classes(self) -> set[type[Glyph]]:
        """Get the expected set of classes that IntersectionCircleGlyph should inherit from.

        Returns:
            set[type[Glyph]]: A set containing the expected classes.
        """
        return {IntersectionCircleGlyph, CircleGlyph, Glyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
