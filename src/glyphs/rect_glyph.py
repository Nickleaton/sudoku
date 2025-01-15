"""RectGlyph."""
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord
from src.utils.point import Point


class RectGlyph(Glyph):
    """Represents a rectangle in SVG format."""

    def __init__(self, class_name: str, location: Coord, dimension: Coord):
        """Initialize a rectangle glyph with a class name, location, and size.

        Args:
            class_name (str): The class name for the SVG element.
            location (Coord): The location of the rectangle.
            dimension (Coord): The size (width and height) of the rectangle.
        """
        super().__init__(class_name)
        self.location: Coord = location
        self.dimension: Coord = dimension
        self.position: Point = Point.create_from_coord(location)
        self.size: Point = Point.create_from_coord(dimension)

    def draw(self) -> Rect:
        """Draw the rectangle using the specified location and size.

        Returns:
            Rect: An SVG `Rect` element representing the rectangle.
        """
        return Rect(transform=self.position.transform, size=self.size.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        """Return a string representation of the RectGlyph.

        Returns:
            str: A string representing the `RectGlyph` instance, including its class name, location, and size.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.location!r}, {self.dimension!r})"
