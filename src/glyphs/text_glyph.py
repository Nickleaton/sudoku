"""TextGlyph."""
from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.container import Group
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle
from src.utils.coord import Coord


class TextGlyph(Glyph):
    """A glyph that represents a text element with rotation and positioning."""

    def __init__(self, class_name: str, angle: float, position: Coord, text: str) -> None:
        """Initialize the TextGlyph.

        Args:
            class_name (str): The CSS class name for styling the glyph.
            angle (float): The angle by which the text will be rotated.
            position (Coord): The position on the canvas where the text will be placed.
            text (str): The actual text content to be displayed.
        """
        super().__init__(class_name)
        self.angle = Angle(angle)
        self.position = position
        self.text = text

    def draw(self) -> Optional[BaseElement]:
        """Draw the text glyph element.

        Returns:
            Optional[BaseElement]: A group containing the foreground and background text elements.
        """
        group = Group()

        # Create background text
        background_text = Text("",
                               transform=self.position.transform + " " + self.angle.transform,
                               class_=self.class_name + "Background"
                               )
        span = TSpan(self.text, alignment_baseline='central', text_anchor='middle')
        background_text.add(span)
        group.add(background_text)

        # Create foreground text
        foreground_text = Text("",
                               transform=self.position.transform + " " + self.angle.transform,
                               class_=self.class_name + "Foreground"
                               )
        span = TSpan(self.text, alignment_baseline='central', text_anchor='middle')
        foreground_text.add(span)
        group.add(foreground_text)

        return group

    def __repr__(self) -> str:
        """Return a string representation of the TextGlyph.

        Returns:
            str: A string representing the TextGlyph with its class name, angle, position, and text.
        """
        return (
            f"{self.__class__.__name__}('{self.class_name}', {self.angle.angle}, {self.position!r}, '{self.text}')"
        )
