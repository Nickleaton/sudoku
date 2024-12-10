"""SimpleThermometerGlyph."""

from typing import Optional

from svgwrite.container import Marker
from svgwrite.shapes import Circle

from src.glyphs.thermometer_glyph import ThermometerGlyph


class SimpleThermometerGlyph(ThermometerGlyph):
    """A simple thermometer glyph with a custom start marker.

    This class extends `ThermometerGlyph` and adds a custom marker at the start of the thermometer,
    along with a string representation method to display essential attributes.

    Attributes:
        class_name (str): The class name for the thermometer glyph.
        coords (list[Coord]): The list of coordinates for the thermometer glyph.
    """

    @classmethod
    def start_marker(cls) -> Optional[Marker]:
        """Create and return a custom marker for the start of the thermometer.

        This marker is used to represent the starting point of the thermometer.

        Returns:
            Optional[Marker]: A Marker object representing the start of the thermometer,
            or None if the marker cannot be created.
        """
        marker = Marker(
            insert=(50, 50),
            viewBox='0 0 100 100',
            id_='SimpleThermometer-start',
            class_='SimpleThermometer SimpleThermometerStart',
        )
        marker.add(Circle(center=(50, 50), r=30))
        return marker

    def __repr__(self) -> str:
        """Return a string representation of the SimpleThermometerGlyph.

        This method provides a concise way to represent the SimpleThermometerGlyph object as a string.

        Returns:
            str: A string representation of the SimpleThermometerGlyph object,
            including the class name and coordinates.
        """
        return (
            f'{self.__class__.__name__}('
            f'{self.class_name!r}, '
            f'[{", ".join([repr(coord) for coord in self.coords])}]'
            f')'
        )
