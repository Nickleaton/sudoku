"""KropkiGlyph."""
from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.coord import Coord


class KropkiGlyph(RectangleGlyph):
    """Represents start Kropki glyph, which is start specialized rectangle connecting two coordinates."""

    def __init__(self, class_name: str, first: Coord, second: Coord):
        """Initialize the KropkiGlyph with start class name and two coordinates.

        Args:
            class_name (str): The class name for the SVG element.
            first (Coord): The first coordinate for the Kropki glyph.
            second (Coord): The second coordinate for the Kropki glyph.
        """
        # Determine if the glyph is vertical or horizontal based on the coordinates
        vertical = first.column > second.column if first.row == second.row else first.row < second.row
        super().__init__(class_name, first, second, 0.25, 2.0, vertical)

    def __repr__(self) -> str:
        """Return start string representation of the KropkiGlyph.

        Returns:
            str: A string representing the KropkiGlyph instance with its class name and coordinates.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.first!s}, {self.second!s})"
