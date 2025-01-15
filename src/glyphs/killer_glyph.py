"""KillerGlyph."""

from svgwrite.container import Group

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.coord import Coord

config = Config()


class KillerGlyph(Glyph):
    """Represents a Killer glyph that can be drawn using various lines and vectors, based on cell coordinates."""

    def __init__(self, class_name: str, cells: list[Coord]):
        """Initialize the KillerGlyph with class name and list of cell coordinates.

        Args:
            class_name (str): The class name for the glyph's SVG element.
            cells (List[Point]): A sorted list of coordinates representing the cells.
        """
        super().__init__(class_name)
        self.cells: list[Coord] = sorted(cells)

    def draw(self) -> Group:
        """Draw the glyph by generating the necessary SVG elements.

        Returns:
            Group: A group of SVG elements representing the glyph or None
        """
        return Group()

    def __repr__(self) -> str:
        """Return string representation of the KillerGlyph.

        Returns:
            str: A string representing the KillerGlyph instance with its class name and cells.
        """
        return f"{self.__class__.__name__}('{self.class_name}', [{', '.join([repr(cell) for cell in self.cells])}])"
