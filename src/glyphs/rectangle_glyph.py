from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph, config
from src.utils.coord import Coord
from src.utils.point import Point


class RectangleGlyph(Glyph):
    """Represents a rectangle glyph that can be drawn on an SVG canvas.

    Attributes:
        class_name (str): CSS class name for the SVG element.
        first (Coord): The first coordinate point of the rectangle.
        second (Coord): The second coordinate point of the rectangle.
        percentage (float): Scale factor relative to cell size.
        ratio (float): Width-to-height ratio for the rectangle.
        vertical (bool): Whether the rectangle is oriented vertically.
    """

    # pylint: disable=too-many-arguments
    def __init__(self,
                 class_name: str,
                 first: Coord,
                 second: Coord,
                 percentage: float,
                 ratio: float,
                 vertical: bool) -> None:
        """Initializes the RectangleGlyph.

        Args:
            class_name (str): CSS class name for styling the rectangle.
            first (Coord): The starting coordinate.
            second (Coord): The ending coordinate.
            percentage (float): The size scale factor relative to cell size.
            ratio (float): Aspect ratio (width/height).
            vertical (bool): Orientation of the rectangle.
        """
        super().__init__(class_name)
        self.first: Coord = first
        self.second: Coord = second
        self.percentage: float = percentage
        self.ratio: float = ratio
        self.vertical: bool = vertical

    def draw(self) -> Optional[BaseElement]:
        """Draws the rectangle glyph on an SVG canvas.

        Returns:
            Optional[BaseElement]: An SVG rectangle element if drawing is possible, otherwise None.
        """
        cell_size: int = 100
        if config.drawing is not None and config.drawing.cell_size is not None:
            cell_size = int(config.drawing.cell_size)

        if self.vertical:
            size = Point(cell_size * self.percentage * self.ratio,
                         cell_size * self.percentage)
        else:
            size = Point(cell_size * self.percentage,
                         cell_size * self.percentage * self.ratio)
        position = Coord.middle(self.first, self.second)
        return Rect(transform=position.transform, size=size.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        """Provides a string representation of the RectangleGlyph instance.

        Returns:
            str: A string representation of the RectangleGlyph.
        """
        return (
            f"{self.__class__.__name__}("
            f"'{self.class_name}', "
            f"{repr(self.first)}, "
            f"{repr(self.second)}, "
            f"{repr(self.percentage)}, "
            f"{repr(self.ratio)}, "
            f"{repr(self.vertical)})"
        )
