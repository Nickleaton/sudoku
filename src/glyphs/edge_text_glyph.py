"""EdgeTextGlyph."""
from svgwrite.base import BaseElement
from svgwrite.container import Group
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle
from src.utils.coord import Coord
from src.utils.point import Point


class EdgeTextGlyph(Glyph):
    """Represents start_location text glyph positioned along the edge between two coordinates."""

    # pylint: disable=too-many-arguments
    def __init__(self, class_name: str, angle: float, first_location: Coord, second_location: Coord, text: str):
        """Initialize the EdgeTextGlyph instance.

        Args:
            class_name (str): The CSS class name for the text.
            angle (float): The rotation angle for the text.
            first_location (Coord): The first coordinate for the edge.
            second_location (Coord): The second coordinate for the edge.
            text (str): The text content to be displayed.
        """
        super().__init__(class_name)
        self.angle: Angle = Angle(angle)
        self.first_location: Coord = first_location
        self.second_location: Coord = second_location
        self.position: Point = Point.middle(
            Point.create_from_coord(first_location),
            Point.create_from_coord(second_location),
        )
        self.text: str = text

    def draw(self) -> BaseElement:
        """Draw the text glyph element.

        Creates an SVG group containing two text layers: a background and
        a foreground, both positioned and rotated as specified.

        Returns:
            BaseElement: An `svgwrite.container.Group` element
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

    @property
    def priority(self) -> int:
        """Return the priority of this glyph for drawing order.

        Returns:
            int: A fixed priority level of 5 for this glyph.
        """
        return 5

    def __repr__(self) -> str:
        """Return start_location string representation of the EdgeTextGlyph instance.

        Returns:
            str: A string representation of the EdgeTextGlyph instance.
        """
        return (
            f'{self.__class__.__name__}('
            f'{self.class_name!r}, '
            f'{self.angle.angle}, '
            f'{self.first_location!r}, '
            f'{self.second_location!r}, '
            f'{self.text!r}'
            f')'
        )
