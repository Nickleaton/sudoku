"""ArrowGlyph."""

from svgwrite.base import BaseElement
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.point import Point

config: Config = Config()


class ArrowGlyph(Glyph):
    """Represents an arrow glyph to be drawn on an SVG canvas."""

    arrow: str = '\u2191'  # Unicode arrow symbol (↑)

    def __init__(self, class_name: str, angle: float, location: Coord) -> None:
        """Initialize an ArrowGlyph instance.

        Args:
            class_name (str): The CSS class name for the SVG element.
            angle (float): The angle of the arrow in degrees.
            location (Coord): The coordinate where the arrow will be drawn.
        """
        super().__init__(class_name)
        self.angle: Angle = Angle(angle)  # Convert angle to an `Angle` object.
        self.location: Coord = location
        self.position: Point = Point.create_from_coord(location) * config.graphics.cell_size

    def draw(self) -> BaseElement | None:
        """Draw the arrow glyph as an SVG text element.

        Returns:
            BaseElement | None: An SVG Text element with the arrow symbol, or None if the
            location is invalid.
        """
        if not self.location:  # Validate the location
            return None

        # Apply location and rotation transformations
        transform: str = f'{self.position.transform} {self.angle.transform}'

        # Create SVG text and span elements
        text: Text = Text('', transform=transform, class_=self.class_name)
        span: TSpan = TSpan(
            ArrowGlyph.arrow,
            alignment_baseline='central',
            text_anchor='middle',
        )
        text.add(span)
        return text

    def __repr__(self) -> str:
        """Return a string representation of the ArrowGlyph instance.

        Returns:
            str: A string representing the class name, angle, and location.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.angle.angle!r}, {self.location!r})'
