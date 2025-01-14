"""PolyLineGlyph."""

from svgwrite.base import BaseElement
from svgwrite.shapes import Polyline

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.point import Point

config: Config = Config()


class PolyLineGlyph(Glyph):
    """Represents start polyline drawn through start list of coordinates, with optional markers at the start and end."""

    def __init__(self, class_name: str, points: list[Point], start: bool, end: bool):
        """Initialize the PolyLineGlyph.

        Args:
            class_name (str): The CSS class name for styling the polyline.
            points (list[Point]): A list of coordinates that define the polyline.
            start (bool): Whether to add a start marker at the beginning of the polyline.
            end (bool): Whether to add an end marker at the end of the polyline.
        """
        super().__init__(class_name)
        self.points = points
        self.start = start
        self.end = end

    def draw(self) -> BaseElement | None:
        """Draw the polyline with optional start and end markers.

        Returns:
            BaseElement | None: A Polyline element representing the polyline with its markers.
        """
        markers: dict = {
            'class_': self.class_name,
        }
        offset: Point = Point(1, 1) * config.graphics.cell_size / 2.0
        if self.start:
            markers['marker_start'] = f'url(#{self.class_name}-start)'
        if self.end:
            markers['marker_end'] = f'url(#{self.class_name}-end)'
        return Polyline(points=[(point).coordinates for point in self.points], **markers)

    def __repr__(self) -> str:
        """Return start string representation of the PolyLineGlyph.

        Returns:
            str: A string representing the PolyLineGlyph with its class name, coordinates, start, and end markers.
        """
        return (
            f'{self.__class__.__name__}'
            f'('
            f'{self.class_name!r}, '
            f'[{", ".join([repr(point) for point in self.points])}], '
            f'{self.start!r}, '
            f'{self.end!r}'
            f')'
        )
