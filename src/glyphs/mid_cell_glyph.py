from typing import Optional
from svgwrite.base import BaseElement
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class MidCellGlyph(Glyph):
    """Represents a glyph for a mid-cell marker in an SVG drawing."""

    def __init__(self, class_name: str, position: Coord):
        """Initialize the MidCellGlyph with a class name and position.

        Args:
            class_name (str): The CSS class name to apply to the glyph.
            position (Coord): The position of the glyph in the grid.
        """
        super().__init__(class_name)
        self.position = position
        self.percentage = 0.7
        self.size = Coord(1, 1) * self.percentage

    def draw(self) -> Optional[BaseElement]:
        """Create an SVG rectangle element representing the mid-cell glyph.

        Returns:
            Optional[BaseElement]: The SVG rectangle element or None.
        """
        top_left = self.position + Coord(1, 1) * (1.0 - self.percentage) / 2.0
        return Rect(transform=top_left.transform, size=self.size.point.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        """Return a string representation of the MidCellGlyph instance.

        Returns:
            str: A string representation of the glyph in the format
                MidCellGlyph('<class_name>', <position>).
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r})"
