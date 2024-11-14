from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class MidCellGlyph(Glyph):
    """Represents a glyph for a middle cell, drawn as a rectangle centered at a given position."""

    def __init__(self, class_name: str, position: Coord):
        """Initialize the MidCellGlyph with the given class name and position.

        Args:
            class_name (str): The class name for the SVG element.
            position (Coord): The coordinates where the glyph will be positioned.
        """
        super().__init__(class_name)
        self.position = position  # The position of the glyph
        self.percentage = 0.7  # Size percentage of the total cell
        self.size = Coord(1, 1) * self.percentage  # Scaled size based on the percentage

    def draw(self) -> Optional[BaseElement]:
        """Draw the MidCellGlyph as a centered rectangle.

        This method calculates the position of the rectangle such that it is centered
        at `self.position` and has the dimensions defined by `self.size`.

        Returns:
            Optional[BaseElement]: An SVG Rect element representing the middle cell glyph.
        """
        # Calculate the top-left position of the rectangle to center it
        top_left = self.position + Coord(1, 1) * (1.0 - self.percentage) / 2.0
        return Rect(transform=top_left.transform, size=self.size.point.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        """Return a string representation of the MidCellGlyph.

        Returns:
            str: A string representing the MidCellGlyph instance with its class name and position.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r})"
