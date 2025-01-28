"""EvenCellGlyph."""

from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.point import Point

config: Config = Config()


class EvenCellGlyph(Glyph):
    """Represents an even cell glyph to be drawn with SVG, inheriting from the Glyph class.

    This glyph represents an "even" cell in a grid and is drawn as a rectangle.
    The size and positioning of the glyph depend on the configuration settings.

    Attributes:
        class_name (str): The CSS class name for the SVG element.
        location (Coord): The location of the glyph in coordinates.
        size (Point): The size of the rectangle (calculated based on configuration).
    """

    def __init__(self, class_name: str, location: Coord):
        """Initialize the EvenCellGlyph with the given class name and location.

        Args:
            class_name (str): The class name for the SVG element.
            location (Coord): The location of the glyph in coordinates.

        Raises:
            ValueError: If the scale digit is invalid
        """
        super().__init__(class_name)
        self.location: Coord = location
        self.position: Point = Point.create_from_coord(self.location)

        # Scaling factor for the rectangle size (calculated from config)
        scale: float = config.graphics.parity_cell.even.size * config.graphics.cell_size

        # Ensure that scale is a valid non-zero digit
        if scale <= 0:
            raise ValueError(f'Invalid scale digit: {scale}. Check configuration.')

        self.size: Point = Point(1, 1) * scale

    def draw(self) -> Rect:
        """Draw the glyph as an SVG rectangle with the appropriate location and size.

        Returns:
            Rect: An SVG Rect element

        Raises:
            ValueError: If the inset digit is invalid
        """
        # Calculate the top-left corner of the rectangle after applying scaling
        inset: float = config.graphics.parity_cell.even.inset * config.graphics.cell_size

        # Ensure the inset digit is valid
        if inset < 0:
            raise ValueError(f'Invalid inset digit: {inset}. Check configuration.')

        top_left: Point = self.position + Point(1, 1) * inset

        return Rect(transform=top_left.transform, size=self.size.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        """Return a string representation of the EvenCellGlyph.

        Returns:
            str: A string representing the EvenCellGlyph instance.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.location!r})'
