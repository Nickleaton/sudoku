"""RectGlyph."""

from svgwrite.base import BaseElement
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class RectGlyph(Glyph):
    """Represents a rectangle in SVG format."""

    def __init__(self, class_name: str, position: Coord, size: Coord):
        """Initialize a rectangle glyph with a class name, position, and size.

        Args:
            class_name (str): The class name for the SVG element.
            position (Coord): The position of the rectangle.
            size (Coord): The size (width and height) of the rectangle.
        """
        super().__init__(class_name)
        self.position = position  # The position of the rectangle
        self.size = size  # The size (width and height) of the rectangle

    def draw(self) -> BaseElement | None:
        """Draw the rectangle using the specified position and size.

        Returns:
            BaseElement | None: An SVG `Rect` element representing the rectangle.
        """
        return Rect(transform=self.position.transform, size=self.size.point.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        """Return a string representation of the RectGlyph.

        Returns:
            str: A string representing the `RectGlyph` instance, including its class name, position, and size.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r}, {self.size!r})"


class SquareGlyph(RectGlyph):
    """Represents a square (a special case of a rectangle with equal width and height) in SVG format."""

    def __init__(self, class_name: str, position: Coord, size: int):
        """Initialize a square glyph with a class name, position, and size.

        Args:
            class_name (str): The class name for the SVG element.
            position (Coord): The position of the square.
            size (int): The size (width and height) of the square.
        """
        super().__init__(class_name, position, Coord(size, size))  # Square has equal width and height

    def __repr__(self) -> str:
        """Return a string representation of the SquareGlyph.

        Returns:
            str: A string representing the `SquareGlyph` instance, including its class name, position, and size.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r}, {self.size.row!r})"


class BoxGlyph(RectGlyph):
    """Represents a box (a rectangle) in SVG format."""

    def __repr__(self) -> str:
        """Return a string representation of the BoxGlyph.

        Returns:
            str: A string representing the `BoxGlyph` instance, including its class name, position, and size.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r}, {self.size!r})"
