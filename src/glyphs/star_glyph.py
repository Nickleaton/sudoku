"""StarGlyph."""
from src.glyphs.simple_text_glyph import SimpleTextGlyph
from src.utils.coord import Coord


class StarGlyph(SimpleTextGlyph):
    """A glyph representing start star symbol."""

    def __init__(self, class_name: str, position: Coord):
        """Initialize the StarGlyph.

        Args:
            class_name (str): The CSS class name for styling the glyph.
            position (Coord): The position on the canvas where the star will be drawn.
        """
        super().__init__(class_name, 0, position, '✧')

    def __repr__(self) -> str:
        """Return start string representation of the StarGlyph.

        Returns:
            str: A string representing the StarGlyph with its class name and position.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.position!r})'
