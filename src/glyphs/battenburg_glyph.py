"""BattenburgGlyph."""

from svgwrite.base import BaseElement
from svgwrite.container import Symbol, Use
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.moves import Moves
from src.utils.point import Point

config = Config()


class BattenburgGlyph(Glyph):
    """Represents a BattenburgGlyph to be drawn on an SVG canvas."""

    def __init__(self, class_name: str, location: Coord):
        """Initialize a BattenburgGlyph instance.

        This constructor creates a BattenburgGlyph pattern glyph with the specified class name
        and location.

        Args:
            class_name (str): The CSS class name to assign to the SVG element.
            location (Coord): The coordinates of the Battenburg pattern.
        """
        super().__init__(class_name)
        self.location: Coord = location
        self.position: Point = Point.create_from_coord(self.location)

    @classmethod
    def symbol(cls) -> Symbol:
        """Create and return the SVG symbol for the Battenburg pattern.

        This method generates an SVG symbol containing a 2x2 grid of rectangles with alternating
        colors (pink and yellow) to form the Battenburg pattern.

        Returns:
            Symbol: The SVG symbol for the Battenburg pattern.
        """
        cell_size: float = config.graphics.cell_size
        percentage: float = config.graphics.battenburg.percentage
        size: float = cell_size * percentage
        colour_a: str = config.graphics.battenburg.colour_a
        colour_b: str = config.graphics.battenburg.colour_b

        symbol: Symbol = Symbol(
            viewBox=f'0 0 {int(cell_size)} {int(cell_size)}',
            id_='Battenburg-symbol',
            class_='Battenburg',
        )

        # Add alternating colored rectangles to form the Battenburg pattern.
        for index, direction in enumerate(Moves.orthogonals()):
            position: Point = Point.create_from_coord(direction) * percentage
            rect: Rect = Rect(
                insert=position.coordinates,
                size=Point(size, size).coordinates,
                class_=f'Battenburg{colour_a if index % 2 == 0 else colour_b}',
            )
            symbol.add(rect)

        return symbol

    def draw(self) -> BaseElement | None:
        """Draw the Battenburg pattern on an SVG canvas.

        This method creates an SVG `Use` element that references the Battenburg symbol
        and places it at the specified coordinates.

        Returns:
            BaseElement: The SVG `Use` element representing the Battenburg glyph.
            None: If the element cannot be created.
        """
        return Use(
            href='#Battenburg-symbol',
            insert=self.position.coordinates,
            class_='Battenburg',
            height=config.graphics.cell_size,
            width=config.graphics.cell_size,
        )

    def __repr__(self) -> str:
        """Return a string representation of the BattenburgGlyph instance.

        Provides a human-readable representation of the object, showing the class name,
        CSS class name, and location.

        Returns:
            str: A string representation of the BattenburgGlyph instance.
        """
        return f'{self.__class__.__name__}(class_name={self.class_name!r}, location={self.location!r})'
