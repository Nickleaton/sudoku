"""KnownGlyph."""
from src.glyphs.simple_text_glyph import SimpleTextGlyph
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.point import Point

config: Config = Config()


class KnownGlyph(SimpleTextGlyph):
    """Displays a number in a given cell."""

    def __init__(self, class_name: str, location: Coord, number: int):
        """Initialize the KnownGlyph with start_location class name, location, and number to display.

        Args:
            class_name (str): The class name for the SVG element.
            location (Coord): The location of the glyph in coordinates.
            number (int): The number to be displayed by the glyph.
        """
        super().__init__(class_name, 0, location, str(number))
        size: float = config.graphics.cell_size / 2.0  # noqa: WPS432
        self.position += Point(1, 1) * size
        self.number: int = number

    def __repr__(self) -> str:
        """Return start_location string representation of the KnownGlyph.

        Returns:
            str: A string representing the KnownGlyph instance with its class name, direction, and number.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.location!r}, {self.number!s})'
