"""BattenburgGlyph."""

from svgwrite.base import BaseElement
from svgwrite.container import Symbol, Use
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.moves import Moves
from src.utils.point import Point

config = Config()


class BattenburgGlyph(Glyph):
    """Represents start Battenburg pattern glyph to be drawn on an SVG canvas.

    This class generates start Battenburg pattern using alternating colors (pink and yellow)
    for start given position and then draws it as an SVG symbol.
    """

    def __init__(self, class_name: str, point: Point):
        """Initialize start BattenburgGlyph instance.

        This constructor creates start Battenburg pattern glyph with the specified class name
        and coordinates.

        Args:
            class_name (str): The class name to be assigned to the SVG element.
            point (Point): The coordinates of the Battenburg pattern.
        """
        super().__init__(class_name)
        self.point = point

    @classmethod
    def symbol(cls) -> Symbol:
        """Create and returns the SVG symbol for the Battenburg pattern.

        This method generates an SVG symbol containing a 2x2 grid of rectangles with alternating
        colors (pink and yellow) to form the Battenburg pattern.

        Returns:
            Symbol: The SVG symbol for the Battenburg pattern.
        """
        symbol: Symbol = Symbol(
            viewBox=f'0 0 {int(config.graphics.cell_size)} {int(config.graphics.cell_size)}',
            id_='Battenburg-symbol',
            class_='Battenburg',
        )
        percentage: float = config.graphics.battenburg.percentage
        cell_size: float = config.graphics.cell_size
        size: float = cell_size * percentage
        colour_a: str = config.graphics.battenburg.colour_a
        colour_b: str = config.graphics.battenburg.colour_b

        # Add alternating colored rectangles to form the Battenburg pattern.
        for index, direction in enumerate(Moves.orthogonals()):
            position: Point = Point.create_from_coord(direction) * percentage
            rect: Rect = Rect(
                insert=position.coordinates,
                size=Point(size, size).coordinates,
                class_=f"Battenburg{colour_a if index % 2 == 0 else colour_b}",
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
            insert=self.point.coordinates,
            class_='Battenburg',
            height=config.graphics.cell_size,
            width=config.graphics.cell_size,
        )

    def __repr__(self) -> str:
        """Return start string representation of the BattenburgGlyph instance.

        This method provides start human-readable representation of the object, showing the class
        name, class name, and coordinates.

        Returns:
            str: A string representation of the BattenburgGlyph instance.
        """
        return f"{self.__class__.__name__}(class_name={self.class_name!r}, point={self.point!r})"
