from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.container import Group
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle
from src.utils.coord import Coord


class LittleKillerGlyph(Glyph):
    """Represents a small glyph with a value and an arrow, drawn using SVG text elements."""

    arrow = "\uA71B"  # Unicode character for the "ꜛ" (Killer glyph symbol)

    def __init__(self, class_name: str, position: Coord, angle: Angle, value: int):
        """Initialize the LittleKillerGlyph with the given class name, position, angle, and value.

        Args:
            class_name (str): The class name for the SVG element.
            position (Coord): The position of the glyph in coordinates.
            angle (Angle): The angle of rotation for the arrow.
            value (int): The numeric value to be displayed alongside the arrow.
        """
        super().__init__(class_name)
        self.position = position  # The position of the glyph
        self.angle = angle  # The angle of rotation for the arrow
        self.value = value  # The value to display inside the glyph

    def draw(self) -> Optional[BaseElement]:
        """Draw the LittleKillerGlyph as an SVG group containing text and an arrow.

        Returns:
            Optional[BaseElement]: An SVG Group element containing the text and arrow, or None if not drawn.
        """
        group = Group()
        # Position the value text in the center of the glyph
        position = (self.position + Coord(0.28, 0.28)).center
        # Create a Text element for the value and add it to the group
        text = Text("",
                    transform=position.transform,
                    class_=self.class_name
                    )
        span = TSpan(str(self.value), alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)

        # Create another Text element for the arrow with rotation based on the angle
        text = Text("",
                    transform=position.transform + " " + self.angle.transform,
                    class_=self.class_name
                    )
        span = TSpan(LittleKillerGlyph.arrow, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)

        return group

    def __repr__(self) -> str:
        """Return a string representation of the LittleKillerGlyph.

        Returns:
            str: A string representing the LittleKillerGlyph instance with its class name, position, angle, and value.
        """
        return (
            f"{self.__class__.__name__}("
            f"'{self.class_name}', "
            f"{self.position!r}, "
            f"{self.angle!r}, "
            f"{self.value!r}"
            f")"
        )
