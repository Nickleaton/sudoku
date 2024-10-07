from typing import List, Optional

from svgwrite.base import BaseElement
from svgwrite.container import Group
from svgwrite.shapes import Line

from src.glyphs.glyph import Glyph, config
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.point import Point
from src.utils.vector import Vector
from src.utils.vector_list import VectorList


class KillerGlyph(Glyph):
    offset = 10

    size = config.drawing.cell_size / 2.0

    long_size = config.drawing.cell_size / 2.0 - offset

    long_lines = {
        2: Vector(Coord(0, 0), Coord(0, 1)),
        4: Vector(Coord(0, 0), Coord(1, 0)),
        6: Vector(Coord(0, 1), Coord(1, 1)),
        8: Vector(Coord(1, 0), Coord(1, 1))
    }

    short_lines = {
        12: (Point(-1, -1), Direction.UP),
        23: (Point(1, -1), Direction.UP),
        36: (Point(1, -1), Direction.RIGHT),
        69: (Point(1, 1), Direction.RIGHT),
        89: (Point(1, 1), Direction.DOWN),
        78: (Point(-1, 1), Direction.DOWN),
        47: (Point(-1, 1), Direction.LEFT),
        14: (Point(-1, -1), Direction.LEFT)
    }

    def __init__(self, class_name: str, cells: List[Coord]):
        super().__init__(class_name)
        self.cells = sorted(cells)

    def outside(self, cell: Coord) -> bool:
        for c in self.cells:
            if cell.row == c.row and cell.column == c.column:
                return False
        return True

    def cell_long_lines(self, cell: Coord) -> VectorList:
        vectors = []
        for location, vector in KillerGlyph.long_lines.items():
            if self.outside(cell + Direction(location).offset):
                vectors.append(vector + cell)
        return VectorList(vectors)

    def lines(self) -> VectorList:
        results = VectorList([])
        for cell in self.cells:
            results += self.cell_long_lines(cell)
        results.sort()
        return results

    def draw(self) -> Optional[BaseElement]:
        group = Group()
        for vector in VectorList.merge_vectors(self.lines()):
            group.add(
                Line(
                    start=vector.start.point.coordinates,
                    end=vector.end.point.coordinates,
                    class_=self.class_name
                )
            )
        return group

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', [{', '.join([repr(cell) for cell in self.cells])}])"
