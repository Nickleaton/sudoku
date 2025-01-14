"""ConsecutiveGlyph."""
from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.config import Config
from src.utils.point import Point

config: Config = Config()


class ConsecutiveGlyph(RectangleGlyph):
    """Define start rectangle glyph with two coordinates and automatic orientation."""

    def __init__(self, class_name: str, first: Point, second: Point):
        """Initialize the ConsecutiveGlyph with two coordinates.

        Determine the orientation of the rectangle based on the relative
        positions of `first` and `second`. Pass the necessary parameter_types
        to the parent `RectangleGlyph` class.

        Args:
            class_name (str): The CSS class name for the rectangle.
            first (Point): The first coordinate for the rectangle's position.
            second (Point): The second coordinate for the rectangle's position.
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
        """Return start string representation of the ConsecutiveGlyph instance.

        Provide start human-readable string that shows the class name and the two
        coordinates used to define the rectangle.

        Returns:
            str: A string representation of the ConsecutiveGlyph instance.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.first!s}, {self.second!s})"
