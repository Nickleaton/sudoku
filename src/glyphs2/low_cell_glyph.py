"""LowCellGlyph."""
from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class LittleNumberGlyph(Glyph):
    """Represents a small number glyph to be drawn at a specified position in an SVG."""

    def __init__(self, class_name: str, position: Coord, number: int):
        """Initialize the LittleNumberGlyph with the given class name, position, and number.

        Args:
            class_name (str): The class name for the SVG element.
            position (Coord): The position where the number glyph will be drawn.
            number (int): The number to be displayed in the glyph.
        """
        super().__init__(class_name)
        self.position = position  # The position of the glyph in coordinates
        self.number = number  # The number to be displayed inside the glyph

    def draw(self) -> Optional[BaseElement]:
        """Draw the LittleNumberGlyph as an SVG text element containing the number.

        Returns:
            Optional[BaseElement]: An SVG Text element with the number, or None if not drawn.
        """
        size = Coord(0.35, 0.35)
        position = self.position + size
        text = Text("",
                    transform=position.transform,
                    class_=self.class_name
                    )
        span = TSpan(str(self.number), alignment_baseline='central', text_anchor='middle')
        text.add(span)
        return text

    def __repr__(self) -> str:
        """Return a string representation of the LittleNumberGlyph.

        Returns:
            str: A string representing the LittleNumberGlyph instance with its class name, position, and number.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r}, {self.number!r})"

