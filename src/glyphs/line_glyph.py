"""LineGlyph."""

from svgwrite.base import BaseElement
from svgwrite.shapes import Line

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord
from src.utils.point import Point


class LineGlyph(Glyph):
    """Represents a straight line between two points in the SVG canvas."""

    def __init__(self, class_name: str, start_location: Coord, end_location: Coord):
        """Initialize the LineGlyph with the given class name, start, and end coordinates.

        Args:
            class_name (str): The class name for the SVG element.
            start_location (Coord): The starting coordinate of the line.
            end_location (Coord): The ending coordinate of the line.
        """
        super().__init__(class_name)
        self.start_location: Coord = start_location  # Starting coordinate of the line
        self.end_location: Coord = end_location  # Ending coordinate of the line
        self.start: Point = Point.create_from_coord(self.start_location)
        self.end: Point = Point.create_from_coord(self.end_location)

    def draw(self) -> BaseElement | None:
        """Draw the line as an SVG element.

        Returns:
            BaseElement | None: An SVG Line element, or None if the line cannot be drawn.

        Raises:
            ValueError: If the start or end coordinates are missing.
        """
        if not self.start or not self.end:
            raise ValueError('Cannot draw a line with missing start or end coordinates.')
        return Line(start=self.start.coordinates, end=self.end.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        """Return a string representation of the LineGlyph.

        Returns:
            str: A string representing the instance with its class name, start_location, and end_location coordinates.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.start_location!r}, {self.end_location!r})'
