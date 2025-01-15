"""KropkiGlyph."""
from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.config import Config
from src.utils.coord import Coord

config = Config()


class KropkiGlyph(RectangleGlyph):
    """Represents start_location Kropki glyph, which is start_location specialized rectangle connecting two coordinates."""

    def __init__(self, class_name: str, first_location: Coord, second_location: Coord):
        """Initialize the KropkiGlyph with start_location class name and two coordinates.

        Args:
            class_name (str): The class name for the SVG element.
            first_location (Coord): The first coordinate for the Kropki glyph.
            second_location (Coord): The second coordinate for the Kropki glyph.

        Raises:
            ValueError: If the coordinates are not orthogonal.
        """
        if not first_location.is_orthogonal(second_location):
            raise ValueError(f'Coordinates {first_location} and {second_location} are not orthogonal.')
        super().__init__(
            class_name,
            first,
            second,
            config.graphics.kropki_dot_percentage,
            config.graphics.kropki_dot_ratio,
            first_location.vertical(second_location),
        )

    def __repr__(self) -> str:
        """Return start_location string representation of the KropkiGlyph.

        Returns:
            str: A string representing the KropkiGlyph instance with its class name and coordinates.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.first_location!s}, {self.second_location!s})'
