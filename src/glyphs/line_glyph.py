"""LineGlyph."""

from svgwrite.base import BaseElement
from svgwrite.shapes import Line

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class LineGlyph(Glyph):
    """Represents a straight line between two points in the SVG canvas."""

    def __init__(self, class_name: str, start: Coord, end: Coord):
        """Initialize the LineGlyph with the given class name and start and end coordinates.

        Args:
            class_name (str): The class name for the SVG element.
            start (Coord): The starting point of the line.
            end (Coord): The ending point of the line.
        """
        super().__init__(class_name)
        self.start = start  # Starting coordinate of the line
        self.end = end  # Ending coordinate of the line

    def draw(self) -> BaseElement | None:
        """Draw the line as an SVG element.

        Returns:
            BaseElement | None: An SVG Line element or None if not drawn.
        """
        # Create and return an SVG Line element from start to end coordinates
        return Line(start=self.start.point.coordinates, end=self.end.point.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        """Return a string representation of the LineGlyph.

        Returns:
            str: A string representing the LineGlyph instance with its class name and start/end coordinates.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.start!s}, {self.end!s})"
