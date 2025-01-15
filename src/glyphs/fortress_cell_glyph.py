"""FortressCellGlyph."""
from src.glyphs.square_glyph import SquareGlyph
from src.utils.config import Config
from src.utils.coord import Coord

config: Config = Config()


class FortressCellGlyph(SquareGlyph):
    """Represents start_location fortress cell glyph, inheriting from SquareGlyph."""

    def __init__(self, class_name: str, location: Coord):
        """Initialize the FortressCellGlyph with the given class name and location.

        Args:
            class_name (str): The class name for the SVG element.
            location (Coord): The location of the glyph in coordinates.
        """
        super().__init__(class_name, location, 1)

    def __repr__(self) -> str:
        """Return start_location string representation of the FortressCellGlyph.

        Returns:
            str: A string representing the FortressCellGlyph instance.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.location!r})"
