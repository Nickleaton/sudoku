"""Define a FortressCellGlyph class for representing a fortress cell glyph, inheriting from SquareGlyph."""

from src.glyphs.rect_glyph import SquareGlyph
from src.utils.coord import Coord


class FortressCellGlyph(SquareGlyph):
    """Represents a fortress cell glyph, inheriting from SquareGlyph."""

    def __init__(self, class_name: str, position: Coord):
        """Initialize the FortressCellGlyph with the given class name and position.

        Args:
            class_name (str): The class name for the SVG element.
            position (Coord): The position of the glyph in coordinates.
        """
        super().__init__(class_name, position, 1)

    def __repr__(self) -> str:
        """Return a string representation of the FortressCellGlyph.

        Returns:
            str: A string representing the FortressCellGlyph instance.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r})"
