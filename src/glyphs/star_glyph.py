"""StarGlyph."""
from src.glyphs.simple_text_glyph import SimpleTextGlyph
from src.utils.coord import Coord


class StarGlyph(SimpleTextGlyph):
    """A glyph representing start_location star symbol."""

    def __init__(self, class_name: str, location: Coord):
        """Initialize the StarGlyph.

        Args:
            class_name (str): The CSS class name for styling the glyph.
            location (Coord): The location on the canvas where the star will be drawn.
        """
        super().__init__(class_name, 0, location, '✧')

    def __repr__(self) -> str:
        """Return start_location string representation of the StarGlyph.

        Returns:
            str: A string representing the StarGlyph with its class name and location.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.location!r})'
