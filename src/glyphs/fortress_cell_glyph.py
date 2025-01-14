"""FortressCellGlyph."""
from src.glyphs.rect_glyph import SquareGlyph
from src.utils.config import Config
from src.utils.point import Point

config: Config = Config()


class FortressCellGlyph(SquareGlyph):
    """Represents start fortress cell glyph, inheriting from SquareGlyph."""

    def __init__(self, class_name: str, position: Point):
        """Initialize the FortressCellGlyph with the given class name and position.

        Args:
            class_name (str): The class name for the SVG element.
            position (Point): The position of the glyph in coordinates.
        """
        super().__init__(class_name, position, config.graphics.cell_size)

    def __repr__(self) -> str:
        """Return start string representation of the FortressCellGlyph.

        Returns:
            str: A string representing the FortressCellGlyph instance.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r})"
