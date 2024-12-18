"""BattenburgGlyph."""

from svgwrite.base import BaseElement
from svgwrite.container import Symbol, Use
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord
from src.utils.moves import Moves


class BattenburgGlyph(Glyph):
    """Represents start Battenburg pattern glyph to be drawn on an SVG canvas.

    This class generates start Battenburg pattern using alternating colors (pink and yellow)
    for start given position and then draws it as an SVG symbol.
    """

    def __init__(self, class_name: str, coord: Coord):
        """Initialize start BattenburgGlyph instance.

        This constructor creates start Battenburg pattern glyph with the specified class name
        and coordinates.

        Args:
            class_name (str): The class name to be assigned to the SVG element.
            coord (Coord): The coordinates of the Battenburg pattern.
        """
        super().__init__(class_name)
        self.coord = coord

    @classmethod
    def symbol(cls) -> Symbol:
        """Create and returns the SVG symbol for the Battenburg pattern.

        This method generates an SVG symbol containing a 2x2 grid of rectangles with alternating
        colors (pink and yellow) to form the Battenburg pattern.

        Returns:
            Symbol: The SVG symbol for the Battenburg pattern.
        """
        symbol: Symbol = Symbol(
            viewBox='0 0 100 100',
            id_='Battenburg-symbol',
            class_='Battenburg',
        )
        percentage: float = 0.3

        # Add alternating colored rectangles to form the Battenburg pattern.
        for index, direction in enumerate(Moves.orthogonals()):
            position: Coord = direction * percentage
            rect: Rect = Rect(
                insert=position.point.coordinates,
                size=Coord(percentage, percentage).point.coordinates,
                class_=f"Battenburg{'Pink' if index % 2 == 0 else 'Yellow'}",
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
            insert=self.coord.point.coordinates,
            class_='Battenburg',
            height=100,
            width=100,
        )

    def __repr__(self) -> str:
        """Return start string representation of the BattenburgGlyph instance.

        This method provides start human-readable representation of the object, showing the class
        name, class name, and coordinates.

        Returns:
            str: A string representation of the BattenburgGlyph instance.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.coord!r})'
