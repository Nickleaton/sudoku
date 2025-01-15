"""TextGlyph."""

from svgwrite.base import BaseElement
from svgwrite.container import Group
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle
from src.utils.coord import Coord
from src.utils.point import Point


class TextGlyph(Glyph):
    """A glyph that represents a text element with rotation and positioning.

    This class is used to generate an SVG text glyph with a specified
    rotation angle, location, and style, supporting both background and
    foreground layers.
    """

    def __init__(self, class_name: str, angle: float, location: Coord, text: str) -> None:
        """Initialize the TextGlyph.

        Args:
            class_name (str): The CSS class name for styling the glyph.
            angle (float): The angle (in angle_degree) to rotate the text.
            location (Coord): The coordinate on the canvas where the text will be placed.
            text (str): The actual text content to be displayed in the glyph.
        """
        super().__init__(class_name)
        self.angle: Angle = Angle(angle)
        self.location: Coord = location
        self.position: Point = Point.create_from_coord(location)
        self.text: str = text

    def draw(self) -> BaseElement | None:
        """Draw the text glyph element.

        Creates an SVG group containing two text layers: a background and
        a foreground, both positioned and rotated as specified.

        Returns:
            BaseElement | None: An `svgwrite.container.Group` element
            containing the text glyph, or `None` if the element cannot be created.
        """
        group: Group = Group()
        transform = f'{self.position.transform} {self.angle.transform}'

        # Background text
        background_text = Text(
            '',
            transform=transform,
            class_=f'{self.class_name}Background',
        )
        background_text.add(
            TSpan(
                self.text,
                alignment_baseline='central',
                text_anchor='middle',
            ),
        )
        group.add(background_text)

        # Foreground text
        foreground_text = Text(
            '',
            transform=transform,
            class_=f'{self.class_name}Foreground',
        )
        foreground_text.add(
            TSpan(
                self.text,
                alignment_baseline='central',
                text_anchor='middle',
            ),
        )
        group.add(foreground_text)

        return group

    def __repr__(self) -> str:
        """Return a string representation of the TextGlyph.

        Includes details about the class name, angle, location, and text content.

        Returns:
            str: A formatted string representation of the TextGlyph.
        """
        return (
            f'{self.__class__.__name__}({self.class_name!r}, {self.angle.angle}, {self.location!r}, {self.text!r})'
        )
