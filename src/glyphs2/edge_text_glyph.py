"""EdgeTextGlyph."""
from src.glyphs.text_glyph import TextGlyph
from src.utils.coord import Coord


class EdgeTextGlyph(TextGlyph):
    """Represents a text glyph positioned along the edge between two coordinates."""

    # pylint: disable=too-many-arguments
    def __init__(self, class_name: str, angle: float, first: Coord, second: Coord, text: str):
        """Initialize the EdgeTextGlyph instance.

        Args:
            class_name (str): The CSS class name for the text.
            angle (float): The rotation angle for the text.
            first (Coord): The first coordinate for the edge.
            second (Coord): The second coordinate for the edge.
            text (str): The text content to be displayed.
        """
        super().__init__(class_name, angle, Coord.middle(first, second), text)
        self.first = first
        self.second = second

    @property
    def priority(self) -> int:
        """Return the priority of this glyph for drawing order.

        Returns:
            int: A fixed priority level of 5 for this glyph.
        """
        return 5

    def __repr__(self) -> str:
        """Return a string representation of the EdgeTextGlyph instance.

        Returns:
            str: A string representation of the EdgeTextGlyph instance.
        """
        return (
            f"{self.__class__.__name__}("
            f"'{self.class_name}', "
            f"{self.angle.angle}, "
            f"{self.first!r}, "
            f"{self.second!r}, "
            f"'{self.text}'"
            f")"
        )

