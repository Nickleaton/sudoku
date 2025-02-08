"""RectangleGlyph."""
from svgwrite.base import BaseElement
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.point import Point

config: Config = Config()


class RectangleGlyph(Glyph):
    """Represents a rectangle with adjustable size and orientation in SVG format."""

    def __init__(
        self,
        class_name: str,
        first_location: Coord,
        second_location: Coord,
        percentage: float,
        ratio: float,
        vertical: bool,
    ) -> None:
        """Initialize the rectangle glyph with location, size percentage, and ratio.

        Args:
            class_name (str): The class name for the SVG element.
            first_location (Coord): The first coordinate for positioning the rectangle.
            second_location (Coord): The second coordinate for positioning the rectangle.
            percentage (float): The percentage of the cell size used for the rectangle's width and height.
            ratio (float): The ratio that affects the size in one direction (height/width or width/height).
            vertical (bool): A flag indicating whether the rectangle is vertical (True) or horizontal (False).
        """
        super().__init__(class_name)
        self.first_location: Coord = first_location
        self.second_location: Coord = second_location
        self.first: Point = Point.create_from_coord(self.first_location)
        self.second: Point = Point.create_from_coord(self.second_location)
        self.percentage: float = percentage
        self.ratio: float = ratio
        self.vertical: bool = vertical

    def draw(self) -> BaseElement:
        """Draw the rectangle based on the given location, size, and orientation.

        Returns:
            BaseElement: An SVG `Rect` element representing the rectangle.
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
        position: Point = Point.middle(self.first, self.second)

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
            location, size, and orientation.
        """
        return (
            f'{self.__class__.__name__}('
            f'{self.class_name!r}, {self.first_location!r}, {self.second_location!r}, '
            f'{self.percentage!r}, {self.ratio!r}, {self.vertical!r})'
        )
