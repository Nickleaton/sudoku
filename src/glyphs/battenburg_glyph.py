"""BattenburgGlyph."""
from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.container import Marker, Symbol, Use
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord
from src.utils.direction import Direction


class BattenburgGlyph(Glyph):
    """Represents a Battenburg pattern glyph to be drawn on an SVG canvas.

    This class generates a Battenburg pattern using alternating colors (pink and yellow)
    for a given position and then draws it as an SVG symbol.
    """

    def __init__(self, class_name: str, coord: Coord):
        """Initialize a BattenburgGlyph instance.

        This constructor creates a Battenburg pattern glyph with the specified class name
        and coordinates.

        Args:
            class_name (str): The class name to be assigned to the SVG element.
            coord (Coord): The coordinates of the Battenburg pattern.

        Returns:
            None
        """
        super().__init__(class_name)
        self.coord = coord

    @classmethod
    def symbol(cls) -> Optional[Marker]:
        """Create and return the SVG symbol for the Battenburg pattern.

        This method generates an SVG symbol containing a 2x2 grid of rectangles with alternating
        colors (pink and yellow) to form the Battenburg pattern.

        Returns:
            Marker: The SVG symbol for the Battenburg pattern.
            None: If the symbol cannot be created.
        """
        result = Symbol(
            viewBox="0 0 100 100",
            id_="Battenberg-symbol",
            class_="Battenberg"
        )
        percentage = 0.3
        # Add alternating colored rectangles to form the Battenburg pattern
        for i, position in enumerate([(d * percentage).point for d in Direction.orthogonals()]):
            result.add(
                Rect(
                    transform=position.transform,
                    size=Coord(percentage, percentage).point.coordinates,
                    class_="Battenberg" + ("Pink" if i % 2 == 0 else "Yellow")
                )
            )
        return result

    def draw(self) -> Optional[BaseElement]:
        """Draw the Battenburg pattern on an SVG canvas.

        This method creates an SVG `Use` element that references the Battenburg symbol
        and places it at the specified coordinates.

        Returns:
            BaseElement: The SVG `Use` element representing the Battenburg glyph.
            None: If the element cannot be created.
        """
        return Use(
            href="#Battenberg-symbol",
            insert=self.coord.point.coordinates,
            class_="Battenberg",
            height=100,
            width=100
        )

    def __repr__(self) -> str:
        """Return a string representation of the BattenburgGlyph instance.

        This method provides a human-readable representation of the object, showing the class
        name, class name, and coordinates.

        Returns:
            str: A string representation of the BattenburgGlyph instance.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.coord!r})"
