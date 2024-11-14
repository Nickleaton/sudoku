from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph, config
from src.utils.coord import Coord
from src.utils.point import Point


class RectangleGlyph(Glyph):
    """Represents a rectangle with adjustable size and orientation in SVG format."""

    def __init__(self,
                 class_name: str,
                 first: Coord,
                 second: Coord,
                 percentage: float,
                 ratio: float,
                 vertical: bool) -> None:
        """Initialize a rectangle glyph with position, size percentage, and ratio.

        Args:
            class_name (str): The class name for the SVG element.
            first (Coord): The first coordinate for positioning the rectangle.
            second (Coord): The second coordinate for positioning the rectangle.
            percentage (float): The percentage of the cell size used for the rectangle's width and height.
            ratio (float): The ratio that affects the size in one direction (height/width or width/height).
            vertical (bool): A flag indicating whether the rectangle is vertical (True) or horizontal (False).
        """
        super().__init__(class_name)
        self.first: Coord = first
        self.second: Coord = second
        self.percentage: float = percentage
        self.ratio: float = ratio
        self.vertical: bool = vertical

    def draw(self) -> Optional[BaseElement]:
        """Draw the rectangle based on the given position, size, and orientation.

        Returns:
            Optional[BaseElement]: An SVG `Rect` element representing the rectangle.
        """
        cell_size: int = 100
        if config.drawing is not None and config.drawing.cell_size is not None:
            cell_size = int(config.drawing.cell_size)

        # Calculate the rectangle's size based on the percentage and ratio
        if self.vertical:
            size = Point(cell_size * self.percentage * self.ratio,
                         cell_size * self.percentage)
        else:
            size = Point(cell_size * self.percentage,
                         cell_size * self.percentage * self.ratio)

        # Position the rectangle in the middle of the first and second coordinates
        position = Coord.middle(self.first, self.second)

        # Return the rectangle as an SVG `Rect` element
        return Rect(transform=position.transform, size=size.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        """Return a string representation of the RectangleGlyph.

        Returns:
            str: A string representing the `RectangleGlyph` instance, including its class name,
            position, size, and orientation.
        """
        return (
            f"{self.__class__.__name__}("
            f"{self.class_name}, "
            f"{self.first!r}, "
            f"{self.second!r}, "
            f"{self.percentage!r}, "
            f"{self.ratio!r}, "
            f"{self.vertical!r})"
        )
