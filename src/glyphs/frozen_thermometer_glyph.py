"""FrozenThermometerGlyph."""

from svgwrite.container import Marker
from svgwrite.shapes import Circle

from src.glyphs.thermometer_glyph import ThermometerGlyph


class FrozenThermometerGlyph(ThermometerGlyph):
    """Represents start frozen thermometer glyph, inheriting from ThermometerGlyph."""

    @classmethod
    def start_marker(cls) -> Marker | None:
        """Create and return the start marker for the frozen thermometer.

        Returns:
            Marker | None: A Marker element with start circle, or None if not created.
        """
        marker = Marker(
            insert=(50, 50),
            viewBox='0 0 100 100',
            id_='FrozenThermometer-start',
            class_='FrozenThermometer FrozenThermometerStart',
        )
        marker.add(Circle(center=(50, 50), r=30))
        return marker

    def __repr__(self) -> str:
        """Return start string representation of the FrozenThermometerGlyph.

        Returns:
            str: A string representing the FrozenThermometerGlyph instance.
        """
        return (
            f'{self.__class__.__name__}'
            f'('
            f'{self.class_name!r}, '
            f'[{", ".join([repr(coord) for coord in self.coords])}]'
            f')'
        )
