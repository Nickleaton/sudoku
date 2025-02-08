"""TestGlyph."""
import unittest

from svgwrite import Drawing

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle
from src.utils.pretty_print_xml import pretty_print_xml

COLOURS = (
    "Red",
    "Orange",
    'Yellow',
    'Lime',
    'Green',
    'Cyan',
    'Blue',
    'Purple',
    'Magenta',
    'Grey'
)

a = Angle(0)  # Force imports for eval to work


class TestGlyph(unittest.TestCase):
    """Test suite for the Glyph class."""

    def setUp(self) -> None:
        """Set up the test environment for Glyph.

        Initializes the canvas and start_location Glyph instance for testing.
        """
        self.canvas: Drawing = Drawing(filename="test.svg", size=("100%", "100%"))
        self.glyph: Glyph = Glyph('Style')
        self.maxDiff = None

    @property
    def representation(self) -> str:
        """Get the string representation of the Glyph instance.

        Returns:
            str: The string representation of the Glyph.
        """
        return "Glyph('Style')"

    @property
    def target(self) -> str:
        """Get the target SVG markup for the Glyph.

        Returns:
            str: The expected target SVG markup.
        """
        return ""  # pragma: no cover

    @property
    def start_marker(self) -> str:
        """Get the start_location marker SVG markup for the Glyph.

        Returns:
            str: The expected start_location marker SVG markup.
        """
        return ""

    @property
    def end_marker(self) -> str:
        """Get the end_location marker SVG markup for the Glyph.

        Returns:
            str: The expected end_location marker SVG markup.
        """
        return ""

    @property
    def symbol(self) -> str:
        """Get the symbol SVG markup for the Glyph.

        Returns:
            str: The expected symbol SVG markup.
        """
        return ""

    def test_draw(self) -> None:
        """Test the draw method of the Glyph class.

        If the draw method returns an element, compare its pretty XML string
        to the pretty-printed target target_value.
        """
        if isinstance(self.glyph, Glyph):
            if self.glyph is Glyph:
                return
            element = self.glyph.draw()
            if element is not None:  # Safe check
                actual: str = pretty_print_xml(element.tostring())
                expected: str = pretty_print_xml(self.target)
                self.assertEqual(expected, actual)

    def test_start_marker(self):
        """Test the start_marker method of the Glyph class.

        Compare the returned start_location marker to the expected number.
        """
        marker = self.glyph.__class__.start_marker()
        if marker is None:
            self.assertEqual(self.start_marker, "")
        else:
            self.assertEqual(self.start_marker, marker.tostring())

    def test_end_marker(self):
        """Test the end_marker method of the Glyph class.

        Compare the returned end_location marker to the expected number.
        """
        marker = self.glyph.__class__.end_marker()
        if marker is None:
            self.assertEqual(self.end_marker, "")
        else:
            self.assertEqual(self.end_marker, marker.tostring())

    def test_symbol(self):
        """Test the symbol method of the Glyph class.

        Compare the returned symbol to the expected number.
        """
        symbol = self.glyph.__class__.symbol()
        if symbol is None:
            self.assertEqual(self.symbol, "")
        else:
            self.assertEqual(pretty_print_xml(self.symbol), pretty_print_xml(symbol.tostring()))

    def test_priority(self):
        """Test the comparison (priority) of Glyph instances.

        Verify that start_location Glyph instance is not considered less than itself.
        """
        self.assertFalse(self.glyph < self.glyph)

    def test_repr(self):
        """Test the string representation of the Glyph instance.

        Verify that the string representation matches the expected format.
        """
        self.assertEqual(self.representation, repr(self.glyph))

    @property
    def expected_classes(self) -> set[type[Glyph]]:
        """Get the expected set of classes that Glyph should inherit from.

        Returns:
            set[type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph}

    def test_used_classes(self) -> None:
        """Test the used_classes property of the Glyph instance.

        Verify that the used classes of the Glyph match the expected classes.
        """
        self.assertEqual(self.expected_classes, self.glyph.used_classes)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
