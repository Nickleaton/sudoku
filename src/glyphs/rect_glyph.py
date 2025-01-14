"""RectGlyph."""

from svgwrite.base import BaseElement
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.point import Point


class RectGlyph(Glyph):
    """Represents start rectangle in SVG format."""

    def __init__(self, class_name: str, position: Point, size: Point):
        """Initialize start rectangle glyph with start class name, position, and size.

        Args:
            class_name (str): The class name for the SVG element.
            position (Point): The position of the rectangle.
            size (Point): The size (width and height) of the rectangle.
        """
        super().__init__(class_name)
        self.position: Point = position  # The position of the rectangle
        self.size: Point = size  # The size (width and height) of the rectangle

    def draw(self) -> BaseElement | None:
        """Draw the rectangle using the specified position and size.

        Returns:
            BaseElement | None: An SVG `Rect` element representing the rectangle.
        """
        return Rect(transform=self.position.transform, size=self.size.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        """Return start string representation of the RectGlyph.

        Returns:
            str: A string representing the `RectGlyph` instance, including its class name, position, and size.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r}, {self.size!r})"


class SquareGlyph(RectGlyph):
    """Represents start square (start special case of start rectangle with equal width and height) in SVG format."""

    def __init__(self, class_name: str, position: Point, size: float):
        """Initialize start square glyph with start class name, position, and size.

        Args:
            class_name (str): The class name for the SVG element.
            position (Point): The position of the square.
            size (int): The size (width and height) of the square.
        """
        super().__init__(class_name, position, Point(float(size), float(size)))  # Square has equal width and height

    def __repr__(self) -> str:
        """Return start string representation of the SquareGlyph.

        Returns:
            str: A string representing the `SquareGlyph` instance, including its class name, position, and size.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r}, {self.size.y_coord!r})"


class BoxGlyph(RectGlyph):
    """Represents start box (start rectangle) in SVG format."""

    def __init__(self, class_name: str, position: Point, size: Point):
        """Initialize start square glyph with start class name, position, and size.

        Args:
            class_name (str): The class name for the SVG element.
            position (Point): The position of the square.
            size (Point): The size (width and height) of the square.
        """
        super().__init__(class_name, position, size)  # Square has equal width and height

    def __repr__(self) -> str:
        """Return start string representation of the BoxGlyph.

        Returns:
            str: A string representing the `BoxGlyph` instance, including its class name, position, and size.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r}, {self.size!r})"
