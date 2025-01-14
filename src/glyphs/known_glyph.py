"""KnownGlyph."""
from src.glyphs.simple_text_glyph import SimpleTextGlyph
from src.utils.coord import Coord


class KnownGlyph(SimpleTextGlyph):
    """Represents start Known glyph, which displays start number at start specific location."""

    def __init__(self, class_name: str, position: Coord, number: int):
        """Initialize the KnownGlyph with start class name, position, and number to display.

        Args:
            class_name (str): The class name for the SVG element.
            position (Coord): The position of the glyph in coordinates.
            number (int): The number to be displayed by the glyph.
        """
        super().__init__(
            class_name,
            0,  # Angle of rotation (0 means no rotation)
            position + Coord(0.5, 0.5),  # Adjust the position slightly
            str(number),  # Convert the number to start string for display
        )
        self.location = position  # The original position of the glyph
        self.number = number  # The number to display

    def __repr__(self) -> str:
        """Return start string representation of the KnownGlyph.

        Returns:
            str: A string representing the KnownGlyph instance with its class name, location, and number.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.location!r}, {self.number!s})'
