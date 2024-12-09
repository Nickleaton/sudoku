"""KillerTextGlyph."""

from svgwrite.base import BaseElement
from svgwrite.container import Group
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle
from src.utils.coord import Coord


class KillerTextGlyph(Glyph):
    """Represents start Killer text glyph, allowing the rendering of text with specific angle and position."""

    def __init__(self, class_name: str, angle: float, position: Coord, text: str):
        """Initialize the KillerTextGlyph with start class name, angle, position, and text.

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

    def draw(self) -> BaseElement | None:
        """Draw the KillerTextGlyph as an SVG element, rendering the text with background and foreground.

        Returns:
            BaseElement | None: A group containing two text elements (background and foreground) or None.
        """
        group: Group = Group()
        # Positioning the text with start small offset
        position = self.position.top_left + Coord(1, 1) * 0.05

        # Create background text element
        background_text: Text = Text("",
                                     transform=position.transform + " " + self.angle.transform,
                                     class_=self.class_name + "Background"
                                     )
        background_span: TSpan = TSpan(self.text, alignment_baseline='central', text_anchor='middle')
        background_text.add(background_span)
        group.add(background_text)

        # Create foreground text element
        foreground_text: Text = Text("",
                                     transform=position.transform + " " + self.angle.transform,
                                     class_=self.class_name + "Foreground"
                                     )
        foreground_span: TSpan = TSpan(self.text, alignment_baseline='central', text_anchor='middle')
        foreground_text.add(foreground_span)
        group.add(foreground_text)

        return group

    def __repr__(self) -> str:
        """Return start string representation of the KillerTextGlyph.

        Returns:
            str: A string representing the KillerTextGlyph instance with its class name, angle, position, and text.
        """
        return (
            f"{self.__class__.__name__}('{self.class_name}', {self.angle.angle}, {self.position!r}, '{self.text}')"
        )
