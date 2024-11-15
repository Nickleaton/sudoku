"""PolyLineGlyph."""
from typing import List, Optional

from svgwrite.base import BaseElement
from svgwrite.shapes import Polyline

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class PolyLineGlyph(Glyph):
    """Represents a polyline drawn through a list of coordinates, with optional markers at the start and end."""

    def __init__(self, class_name: str, coords: List[Coord], start: bool, end: bool):
        """Initialize the PolyLineGlyph.

        Args:
            class_name (str): The CSS class name for styling the polyline.
            coords (List[Coord]): A list of coordinates that define the polyline.
            start (bool): Whether to add a start marker at the beginning of the polyline.
            end (bool): Whether to add an end marker at the end of the polyline.
        """
        super().__init__(class_name)
        self.coords = coords
        self.start = start
        self.end = end

    def draw(self) -> Optional[BaseElement]:
        """Draw the polyline with optional start and end markers.

        Returns:
            Optional[BaseElement]: A Polyline element representing the polyline with its markers.
        """
        parameters = {
            'class_': self.class_name
        }
        if self.start:
            parameters['marker_start'] = f"url(#{self.class_name}-start)"
        if self.end:
            parameters['marker_end'] = f"url(#{self.class_name}-end)"
        return Polyline(points=[coord.center.point.coordinates for coord in self.coords], **parameters)

    def __repr__(self) -> str:
        """Return a string representation of the PolyLineGlyph.

        Returns:
            str: A string representing the PolyLineGlyph with its class name, coordinates, start, and end markers.
        """
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}], "
            f"{self.start!r}, "
            f"{self.end!r}"
            f")"
        )
