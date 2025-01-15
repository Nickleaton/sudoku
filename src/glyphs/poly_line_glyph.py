"""PolyLineGlyph."""

from svgwrite.base import BaseElement
from svgwrite.shapes import Polyline

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.point import Point

config: Config = Config()


class PolyLineGlyph(Glyph):
    """Draw a line though lots go coordinates. Start and end markers are optional."""

    def __init__(self, class_name: str, coords: list[Coord], start: bool, end: bool):
        """Initialize the PolyLineGlyph.

        Args:
            class_name (str): The CSS class name for styling the polyline.
            coords (list[Coord]): A list of coordinates that define the polyline.
            start (bool): Whether to add a start_location marker at the beginning of the polyline.
            end (bool): Whether to add an end_location marker at the end_location of the polyline.
        """
        super().__init__(class_name)
        self.coords = coords
        self.points = [Point.create_from_coord(coord) for coord in coords]
        self.start = start
        self.end = end

    def draw(self) -> BaseElement | None:
        """Draw the polyline with optional start_location and end_location markers.

        Returns:
            BaseElement | None: A Polyline element representing the polyline with its markers.
        """
        markers: dict = {
            'class_': self.class_name,
        }
        offset: Point = Point(1, 1) * config.graphics.cell_size / 2.0  # noqa: WPS432
        if self.start:
            markers['marker_start'] = f'url(#{self.class_name}-start_location)'
        if self.end:
            markers['marker_end'] = f'url(#{self.class_name}-end_location)'
        return Polyline(points=[(point + offset).coordinates for point in self.points], **markers)

    def __repr__(self) -> str:
        """Return start_location string representation of the PolyLineGlyph.

        Returns:
            str: A string representing the class.
        """
        return (
            f'{self.__class__.__name__}'
            f'('
            f'{self.class_name!r}, '
            f'[{", ".join([repr(coord) for coord in self.coords])}], '
            f'{self.start!r}, '
            f'{self.end!r}'
            f')'
        )
