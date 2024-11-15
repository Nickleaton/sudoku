"""LittleArrowGlyph."""
from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord
from src.utils.direction import Direction


class LittleArrowGlyph(Glyph):
    """Represents a small arrow glyph, drawn using an SVG text element."""

    arrow = "\u25B2"  # Unicode character for the upward triangle (▲)

    def __init__(self, class_name: str, position: Coord, location: int):
        """Initialize the LittleArrowGlyph with the given class name, position, and direction.

        Args:
            class_name (str): The class name for the SVG element.
            position (Coord): The position of the glyph in coordinates.
            location (int): The direction of the arrow (used to calculate the angle).
        """
        super().__init__(class_name)
        self.position = position  # The position of the glyph
        self.location = location  # The direction of the arrow (angle)

    def draw(self) -> Optional[BaseElement]:
        """Draw the arrow glyph as an SVG text element with a direction.

        Returns:
            Optional[BaseElement]: An SVG Text element containing the arrow symbol or None if not drawn.
        """
        # Determine the direction using the location value
        direction = Direction.direction(self.location)
        # Define the size of the glyph
        size = Coord(0.4, 0.4)
        position = self.position + size  # Adjust position by the size of the arrow
        # Create an SVG Text element to represent the arrow
        text = Text("",
                    transform=position.transform + " " + direction.angle.transform,
                    class_=self.class_name
                    )
        # Create a TSpan for the arrow symbol and add it to the text element
        span = TSpan(LittleArrowGlyph.arrow, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        return text

    def __repr__(self) -> str:
        """Return a string representation of the LittleArrowGlyph.

        Returns:
            str: A string representing the LittleArrowGlyph instance with its class name, position, and location.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r}, {self.location!r})"

