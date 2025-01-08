"""RectangleGlyph."""
from svgwrite.base import BaseElement
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph, config
from src.utils.coord import Coord
from src.utils.point import Point


class RectangleGlyph(Glyph):
    """Represents a rectangle with adjustable size and orientation in SVG format."""

    def __init__(
        self,
        class_name: str,
        first: Coord,
        second: Coord,
        percentage: float,
        ratio: float,
        vertical: bool,
    ) -> None:
        """Initialize the rectangle glyph with position, size percentage, and ratio.

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

    def draw(self) -> BaseElement | None:
        """Draw the rectangle based on the given position, size, and orientation.

        Returns:
            BaseElement | None: An SVG `Rect` element representing the rectangle.
        """
        cell_size = config.graphics.cell_size

        # Calculate the rectangle's size based on the percentage and ratio
        size = (
            Point(
                cell_size * self.percentage * self.ratio,
                cell_size * self.percentage,
            )
            if self.vertical
            else Point(
                cell_size * self.percentage,
                cell_size * self.percentage * self.ratio,
            )
        )

        # Position the rectangle in the middle of the first and second coordinates
        position: Coord = Coord.middle(self.first, self.second)

        # Return the rectangle as an SVG `Rect` element
        return Rect(
            transform=position.transform,
            size=size.coordinates,
            class_=self.class_name,
        )

    def __repr__(self) -> str:
        """Return the string representation of the RectangleGlyph.

        Returns:
            str: A string representing the `RectangleGlyph` instance, including its class name,
            position, size, and orientation.
        """
        return (
            f'{self.__class__.__name__}('
            f'{self.class_name!r}, {self.first!r}, {self.second!r}, '
            f'{self.percentage!r}, {self.ratio!r}, {self.vertical!r})'
        )
