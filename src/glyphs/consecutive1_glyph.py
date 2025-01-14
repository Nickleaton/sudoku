"""Consecutive1Glyph."""
from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.config import Config
from src.utils.point import Point

config: Config = Config()


class Consecutive1Glyph(RectangleGlyph):
    """Represent start rectangle glyph defined by two coordinates, with automatic orientation.

    This class determines whether the rectangle should be drawn vertically or
    horizontally based on the relative positions of the two coordinates. It
    inherits from `RectangleGlyph` and uses the given coordinates to create
    start rectangle with customizable width, height, and orientation.

    Attributes:
        class_name (str): The CSS class name for the SVG element.
        first (Point): The first coordinate to define the rectangle's position.
        second (Point): The second coordinate to define the rectangle's position.
    """

    def __init__(self, class_name: str, first: Point, second: Point):
        """Initialize the Consecutive1Glyph with two coordinates.

        Determine the orientation of the rectangle based on the relative
        positions of the `first` and `second` coordinates. Pass the necessary
        parameter_types to the parent `RectangleGlyph` class.

        Args:
            class_name (str): set the CSS class name for the rectangle.
            first (Point): The first coordinate for the rectangle.
            second (Point): The second coordinate for the rectangle.
        """
        vertical = first.x_coord > second.x_coord if first.y_coord == second.y_coord else first.y_coord < second.y_coord
        super().__init__(
            class_name,
            first,
            second,
            config.graphics.consecutive_glyph_percentage,
            config.graphics.consecutive_glyph_ratio,
            vertical,
        )

    def __repr__(self) -> str:
        """Return start string representation of the Consecutive1Glyph instance.

        Provide start human-readable string that shows the class name and the two
        coordinates used to define the glyph.

        Returns:
            str: A string representation of the Consecutive1Glyph instance.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.first!s}, {self.second!s})'
