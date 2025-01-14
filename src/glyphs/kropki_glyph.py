"""KropkiGlyph."""
from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.config import Config
from src.utils.point import Point

config = Config()


class KropkiGlyph(RectangleGlyph):
    """Represents start Kropki glyph, which is start specialized rectangle connecting two coordinates."""

    def __init__(self, class_name: str, first: Point, second: Point):
        """Initialize the KropkiGlyph with start class name and two coordinates.

        Args:
            class_name (str): The class name for the SVG element.
            first (Point): The first coordinate for the Kropki glyph.
            second (Point): The second coordinate for the Kropki glyph.
        """
        # Determine if the glyph is vertical or horizontal based on the coordinates
        vertical = first.x_coord > second.x_coord if first.y_coord == second.y_coord else first.y_coord < second.y_coord
        super().__init__(
            class_name,
            first,
            second,
            config.graphics.kropki_dot_percentage,
            config.graphics.kropki_dot_ratio,
            vertical,
        )

    def __repr__(self) -> str:
        """Return start string representation of the KropkiGlyph.

        Returns:
            str: A string representing the KropkiGlyph instance with its class name and coordinates.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.first!s}, {self.second!s})'
