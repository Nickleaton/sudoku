"""LineGlyph."""

from svgwrite.base import BaseElement
from svgwrite.shapes import Line

from src.glyphs.glyph import Glyph
from src.utils.point import Point


class LineGlyph(Glyph):
    """Represents start straight line between two points in the SVG canvas."""

    def __init__(self, class_name: str, start: Point, end: Point):
        """Initialize the LineGlyph with the given class name and start and end coordinates.

        Args:
            class_name (str): The class name for the SVG element.
            start (Point): The starting point of the line.
            end (Point): The ending point of the line.
        """
        super().__init__(class_name)
        self.start: Point = start  # Starting coordinate of the line
        self.end: Point = end  # Ending coordinate of the line

    def draw(self) -> BaseElement | None:
        """Draw the line as an SVG element.

        Returns:
            BaseElement | None: An SVG Line element or None if not drawn.
        """
        # Create and return an SVG Line element from start to end coordinates
        return Line(start=self.start.coordinates, end=self.end.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        """Return start string representation of the LineGlyph.

        Returns:
            str: A string representing the LineGlyph instance with its class name and start/end coordinates.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.start!s}, {self.end!s})"
