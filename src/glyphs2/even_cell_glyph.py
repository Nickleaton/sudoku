"""EvenCellGlyph."""
from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class EvenCellGlyph(Glyph):
    """Represents an even cell glyph to be drawn with SVG, inheriting from the Glyph class."""

    def __init__(self, class_name: str, position: Coord):
        """Initialize the EvenCellGlyph with the given class name and position.

        Args:
            class_name (str): The class name for the SVG element.
            position (Coord): The position of the glyph in coordinates.
        """
        super().__init__(class_name)
        self.position = position  # The position of the glyph
        self.percentage = 0.7  # Scaling factor for the size of the glyph
        self.size = Coord(1, 1) * self.percentage  # Scaled size of the glyph

    def draw(self) -> Optional[BaseElement]:
        """Draw the glyph as an SVG rectangle with the appropriate position and size.

        Returns:
            Optional[BaseElement]: An SVG BaseElement (a rectangle) or None if not drawn.
        """
        # Calculate the top-left corner of the rectangle after applying scaling
        top_left = self.position + Coord(1, 1) * (1.0 - self.percentage) / 2.0
        # Return an SVG rectangle element
        return Rect(transform=top_left.transform, size=self.size.point.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        """Return a string representation of the EvenCellGlyph.

        Returns:
            str: A string representing the EvenCellGlyph instance.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r})"

