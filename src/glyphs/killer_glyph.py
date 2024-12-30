"""KillerGlyph."""

from typing import ClassVar

from svgwrite.base import BaseElement
from svgwrite.container import Group

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.moves import Moves
from src.utils.point import Point
from src.utils.vector import Vector
from src.utils.vector_list import VectorList

config = Config()


class KillerGlyph(Glyph):
    """Represents a Killer glyph that can be drawn using various lines and vectors, based on cell coordinates."""

    offset: int = 10
    size: float = config.drawing.cell_size * config.graphics.middle_percentage
    long_size: float = config.drawing.cell_size * config.graphics.middle_percentage - offset

    long_lines: ClassVar[dict[int, Vector]] = {
        2: Vector(Coord(0, 0), Coord(0, 1)),
        4: Vector(Coord(0, 0), Coord(1, 0)),
        6: Vector(Coord(0, 1), Coord(1, 1)),
        8: Vector(Coord(1, 0), Coord(1, 1)),
    }

    short_lines: ClassVar[dict[int, tuple[Point, Coord]]] = {
        12: (Point(-1, -1), Moves.up),
        23: (Point(1, -1), Moves.up),
        36: (Point(1, -1), Moves.right),
        69: (Point(1, 1), Moves.right),
        89: (Point(1, 1), Moves.down),
        78: (Point(-1, 1), Moves.down),
        47: (Point(-1, 1), Moves.left),
        14: (Point(-1, -1), Moves.left),
    }

    def __init__(self, class_name: str, cells: list[Coord]):
        """Initialize the KillerGlyph with class name and list of cell coordinates.

        Args:
            class_name (str): The class name for the glyph's SVG element.
            cells (List[Coord]): A sorted list of coordinates representing the cells.
        """
        super().__init__(class_name)
        self.cells: list[Coord] = sorted(cells)

    def outside(self, start_cell: Coord) -> bool:
        """Check if the given cell is outside the current set of glyph cells.

        Args:
            start_cell (Coord): The coordinate to check.

        Returns:
            bool: True if the cell is outside, otherwise False.
        """
        for cell in self.cells:
            if start_cell.row == cell.row and start_cell.column == cell.column:
                return False
        return True

    def cell_long_lines(self, cell: Coord) -> VectorList:
        """Generate long line vectors for the given cell.

        Args:
            cell (Coord): The coordinate of the cell.

        Returns:
            VectorList: A list of vectors representing long lines for the cell.
        """
        vectors: list[Vector] = []
        for location, vector in KillerGlyph.long_lines.items():
            if self.outside(cell + Moves.directions()[location].offset):
                vectors.append(vector + cell)
        return VectorList(vectors)

    def lines(self) -> VectorList:
        """Generate all the lines for the glyph, based on its cells.

        Returns:
            VectorList: A sorted list of all vectors for the glyph's lines.
        """
        all_vectors: VectorList = VectorList()
        for cell in self.cells:
            all_vectors.extend(self.cell_long_lines(cell))
        return all_vectors

    def draw(self) -> BaseElement | None:
        """Draw the glyph by generating the necessary SVG elements.

        Returns:
            BaseElement | None: A group of SVG elements representing the glyph or None
        """
        return Group()

    def __repr__(self) -> str:
        """Return string representation of the KillerGlyph.

        Returns:
            str: A string representing the KillerGlyph instance with its class name and cells.
        """
        return f"{self.__class__.__name__}('{self.class_name}', [{', '.join([repr(cell) for cell in self.cells])}])"
