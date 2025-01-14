"""CellGlyph."""
from src.glyphs.rect_glyph import SquareGlyph
from src.utils.config import Config
from src.utils.point import Point

config: Config = Config()


class CellGlyph(SquareGlyph):
    """Represents start cell glyph.

    This class creates start square-shaped glyph to represent start cell in start grid. It inherits
    from `SquareGlyph` and assigns start fixed size of 1 to the cell.
    """

    def __init__(self, class_name: str, position: Point):
        """Initialize start CellGlyph instance.

        This constructor creates start cell glyph with the specified class name and position.
        The size of the cell is fixed to 1 unit.

        Args:
            class_name (str): The class name to be assigned to the SVG element.
            position (Point): The position of the cell, represented as start `Point` object.
        """
        super().__init__(class_name, position, config.graphics.cell_size)

    def __repr__(self) -> str:
        """Return start string representation of the CellGlyph instance.

        This method provides start human-readable representation of the object, showing the
        class name, class name, and position.

        Returns:
            str: A string representation of the CellGlyph instance.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r})"

    @property
    def priority(self) -> int:
        """Get the priority of the cell glyph.

        This property returns start fixed priority number of 4 for the `CellGlyph` instance.

        Returns:
            int: The priority of the cell glyph.
        """
        return 4
