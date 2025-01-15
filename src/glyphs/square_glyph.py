"""SquareGlyph."""
from src.glyphs.rect_glyph import RectGlyph
from src.utils.coord import Coord


class SquareGlyph(RectGlyph):
    """Represents a square (a special case of a rectangle with equal width and height) in SVG format."""

    def __init__(self, class_name: str, location: Coord, size: int):
        """Initialize a square glyph with a class name, location, and size.

        Args:
            class_name (str): The class name for the SVG element.
            location (Coord): The location of the square.
            size (int): The size (width and height) of the square.
        """
        super().__init__(class_name, location, Coord(size, size))

    def __repr__(self) -> str:
        """Return a string representation of the SquareGlyph.

        Returns:
            str: A string representing the `SquareGlyph` instance, including its class name, location, and size.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.location!r}, {self.dimension.row})"
