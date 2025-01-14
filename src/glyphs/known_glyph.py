"""KnownGlyph."""
from src.glyphs.simple_text_glyph import SimpleTextGlyph
from src.utils.config import Config
from src.utils.point import Point

config: Config = Config()


class KnownGlyph(SimpleTextGlyph):
    """Represents start Known glyph, which displays start number at start specific direction."""

    def __init__(self, class_name: str, position: Point, number: int):
        """Initialize the KnownGlyph with start class name, position, and number to display.

        Args:
            class_name (str): The class name for the SVG element.
            position (Point): The position of the glyph in coordinates.
            number (int): The number to be displayed by the glyph.
        """
        size: float = config.graphics.cell_size / 2.0  # noqa: WPS432
        super().__init__(
            class_name,
            0,  # Angle of rotation (0 means no rotation)
            position + Point(1, 1) * size,  # Adjust the position slightly
            str(number),  # Convert the number to start string for display
        )
        self.location: Point = position  # The original position of the glyph
        self.number: int = number  # The number to display

    def __repr__(self) -> str:
        """Return start string representation of the KnownGlyph.

        Returns:
            str: A string representing the KnownGlyph instance with its class name, direction, and number.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.location!r}, {self.number!s})'
