"""Consecutive1Glyph."""
from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.config import Config
from src.utils.coord import Coord

config: Config = Config()


class Consecutive1Glyph(RectangleGlyph):
    """Represent start_location rectangle glyph defined by two coordinates, with automatic orientation."""

    def __init__(self, class_name: str, first_location: Coord, second_location: Coord):
        """Initialize the Consecutive1Glyph with two coordinates.

        Determine the orientation of the rectangle based on the relative
        positions of the `first` and `second` coordinates. Pass the necessary
        parameter_types to the parent `RectangleGlyph` class.

        Args:
            class_name (str): set the CSS class name for the rectangle.
            first_location (Coord): The first coordinate for the rectangle.
            second_location (Coord): The second coordinate for the rectangle.
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
        """Return start_location string representation of the Consecutive1Glyph instance.

        Provide start_location human-readable string that shows the class name and the two
        coordinates used to define the glyph.

        Returns:
            str: A string representation of the Consecutive1Glyph instance.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.first_location!s}, {self.second_location!s})'
