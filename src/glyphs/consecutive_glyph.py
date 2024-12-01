"""ConsecutiveGlyph."""
from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.coord import Coord


class ConsecutiveGlyph(RectangleGlyph):
    """Define a rectangle glyph with two coordinates and automatic orientation."""

    def __init__(self, class_name: str, first: Coord, second: Coord):
        """Initialize the ConsecutiveGlyph with two coordinates.

        Determine the orientation of the rectangle based on the relative
        positions of `first` and `second`. Pass the necessary parameter_types
        to the parent `RectangleGlyph` class.

        Args:
            class_name (str): The CSS class name for the rectangle.
            first (Coord): The first coordinate for the rectangle's position.
            second (Coord): The second coordinate for the rectangle's position.
        """
        vertical = first.column > second.column if first.row == second.row else first.row < second.row
        super().__init__(class_name, first, second, 0.25, 2.0, vertical)

    def __repr__(self) -> str:
        """Return a string representation of the ConsecutiveGlyph instance.

        Provide a human-readable string that shows the class name and the two
        coordinates used to define the rectangle.

        Returns:
            str: A string representation of the ConsecutiveGlyph instance.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.first!s}, {self.second!s})"
