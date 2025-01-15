"""KillerTextGlyph."""

from svgwrite.container import Group
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.point import Point

config: Config = Config()


class KillerTextGlyph(Glyph):
    """Represents a Killer text glyph, allowing the rendering of text with specific angle and location."""

    def __init__(self, class_name: str, angle: float, location: Coord, text: str) -> None:
        """Initialize the KillerTextGlyph with class name, angle, location, and text.

        Args:
            class_name (str): The class name for the SVG element.
            angle (float): The rotation angle for the text in angle_degree.
            location (Coord): The location of the text in coordinates.
            text (str): The text content to be displayed.
        """
        super().__init__(class_name)
        self.angle: Angle = Angle(angle)
        self.location: Coord = location
        self.position: Point = Point.create_from_coord(location)
        self.text: str = text

    def draw(self) -> Group | None:
        """Draw the KillerTextGlyph as an SVG element, rendering the text with background and foreground.

        Returns:
            Group | None: A group containing two text elements (background and foreground) or None if not created.
        """
        group: Group = Group()

        # Apply a small offset to the text location
        size: float = config.graphics.killer.text.offset_percentage * config.graphics.cell_size
        position: Point = self.position + Point(1, 1) * size
        transform = f'{position.transform} {self.angle.transform}'

        # Create background text element
        background_text = Text(
            '',
            transform=transform,
            class_=f'{self.class_name}Background',
        )
        background_span = TSpan(self.text, alignment_baseline='central', text_anchor='middle')
        background_text.add(background_span)
        group.add(background_text)

        # Create foreground text element
        foreground_text = Text(
            '',
            transform=transform,
            class_=f'{self.class_name}Foreground',
        )
        foreground_span = TSpan(self.text, alignment_baseline='central', text_anchor='middle')
        foreground_text.add(foreground_span)
        group.add(foreground_text)

        return group

    def __repr__(self) -> str:
        """Return a string representation of the KillerTextGlyph.

        Returns:
            str: A string representing the KillerTextGlyph instance with its class name, angle, location, and text.
        """
        return (
            f'{self.__class__.__name__}({self.class_name!r}, {self.angle.angle}, {self.location!r}, {self.text!r})'
        )
