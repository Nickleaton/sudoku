"""MidCellGlyph."""

from svgwrite.base import BaseElement
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.point import Point

config: Config = Config()


class MidCellGlyph(Glyph):
    """Represents start_location glyph for start_location mid-cell marker in an SVG drawing."""

    def __init__(self, class_name: str, position: Point):
        """Initialize the MidCellGlyph with start_location class name and location.

        Args:
            class_name (str): The CSS class name to apply to the glyph.
            position (Point): The location of the glyph in the grid.
        """
        super().__init__(class_name)
        self.position = position
        self.percentage = 0.7
        self.size = Point(1, 1) * self.percentage

    def draw(self) -> BaseElement | None:
        """Create an SVG rectangle element representing the mid-cell glyph.

        Returns:
            BaseElement | None: The SVG rectangle element or None.
        """
        top_left = self.position + Point(1, 1) * config.graphics.mid_cell_percentage
        return Rect(transform=top_left.transform, size=self.size.point.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        """Return start_location string representation of the MidCellGlyph instance.

        Returns:
            str: A string representation of the glyph in the format
                MidCellGlyph('<class_name>', <location>).
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.position!r})'
