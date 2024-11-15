"""KillerTextGlyph."""
from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.container import Group
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle
from src.utils.coord import Coord


class KillerTextGlyph(Glyph):
    """Represents a Killer text glyph, allowing the rendering of text with specific angle and position."""

    def __init__(self, class_name: str, angle: float, position: Coord, text: str):
        """Initialize the KillerTextGlyph with a class name, angle, position, and text.

        Args:
            class_name (str): The class name for the SVG element.
            angle (float): The rotation angle for the text.
            position (Coord): The position of the text in coordinates.
            text (str): The text content to be displayed.
        """
        super().__init__(class_name)
        self.angle = Angle(angle)  # The angle of rotation for the text
        self.position = position  # The position of the text in coordinates
        self.text = text  # The text content to display

    def draw(self) -> Optional[BaseElement]:
        """Draw the KillerTextGlyph as an SVG element, rendering the text with background and foreground.

        Returns:
            Optional[BaseElement]: A group containing two text elements (background and foreground) or None.
        """
        group = Group()
        # Positioning the text with a small offset
        position = self.position.top_left + Coord(1, 1) * 0.05

        # Create background text element
        text = Text("",
                    transform=position.transform + " " + self.angle.transform,
                    class_=self.class_name + "Background"
                    )
        span = TSpan(self.text, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)

        # Create foreground text element
        text = Text("",
                    transform=position.transform + " " + self.angle.transform,
                    class_=self.class_name + "Foreground"
                    )
        span = TSpan(self.text, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)

        return group

    def __repr__(self) -> str:
        """Return a string representation of the KillerTextGlyph.

        Returns:
            str: A string representing the KillerTextGlyph instance with its class name, angle, position, and text.
        """
        return (
            f"{self.__class__.__name__}('{self.class_name}', {self.angle.angle}, {self.position!r}, '{self.text}')"
        )

