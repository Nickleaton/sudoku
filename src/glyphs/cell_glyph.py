"""CellGlyph."""
from src.glyphs.square_glyph import SquareGlyph
from src.utils.config import Config
from src.utils.coord import Coord

config: Config = Config()


class CellGlyph(SquareGlyph):
    """Represents a cell glyph in a grid.

    This class creates a square-shaped glyph to represent a cell in a grid. It inherits
    from `SquareGlyph` and assigns a fixed size of 1 unit to the cell.
    """

    def __init__(self, class_name: str, location: Coord):
        """Initialize a CellGlyph instance.

        This constructor creates a cell glyph with the specified class name and location.
        The size of the cell is fixed to 1 unit.

        Args:
            class_name (str): The class name to be assigned to the SVG element.
            location (Coord): The location of the cell, represented as a `Coord` object.
        """
        super().__init__(class_name, location, 1)

    def __repr__(self) -> str:
        """Return a string representation of the CellGlyph instance.

        This method provides a human-readable representation of the object, showing the
        class name, class name, and location.

        Returns:
            str: A string representation of the CellGlyph instance.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.location!r})"

    @property
    def priority(self) -> int:
        """Get the priority of the cell glyph.

        This property returns a fixed priority number of 4 for the `CellGlyph` instance.

        Returns:
            int: The priority of the cell glyph.
        """
        return 4
