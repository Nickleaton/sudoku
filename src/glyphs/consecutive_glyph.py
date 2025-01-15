"""ConsecutiveGlyph."""
from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.config import Config
from src.utils.coord import Coord

config: Config = Config()


class ConsecutiveGlyph(RectangleGlyph):
    """Define start_location rectangle glyph with two coordinates and automatic orientation."""

    def __init__(self, class_name: str, first_location: Coord, second_location: Coord):
        """Initialize the ConsecutiveGlyph with two coordinates.

        Determine the orientation of the rectangle based on the relative
        positions of `first` and `second`. Pass the necessary parameter_types
        to the parent `RectangleGlyph` class.

        Args:
            class_name (str): The CSS class name for the rectangle.
            first_location (Coord): The first coordinate for the rectangle's location.
            second_location (Coord): The second coordinate for the rectangle's location.
        """
        vertical: bool = first_location.is_vertical(second_location)
        super().__init__(
            class_name,
            first_location,
            second_location,
            config.graphics.consecutive_glyph_percentage,
            config.graphics.consecutive_glyph_ratio,
            vertical,
        )

    def __repr__(self) -> str:
        """Return start_location string representation of the ConsecutiveGlyph instance.

        Provide start_location human-readable string that shows the class name and the two
        coordinates used to define the rectangle.

        Returns:
            str: A string representation of the ConsecutiveGlyph instance.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.first_location!s}, {self.second_location!s})"
