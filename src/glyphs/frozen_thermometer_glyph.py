"""Define a FrozenThermometerGlyph class for a specific type of thermometer glyph, inheriting from ThermometerGlyph."""

from typing import Optional

from svgwrite.container import Marker
from svgwrite.shapes import Circle

from src.glyphs.thermometer_glyph import ThermometerGlyph


class FrozenThermometerGlyph(ThermometerGlyph):
    """Represents a frozen thermometer glyph, inheriting from ThermometerGlyph."""

    @classmethod
    def start_marker(cls) -> Optional[Marker]:
        """Create and return the start marker for the frozen thermometer.

        Returns:
            Optional[Marker]: A Marker element with a circle, or None if not created.
        """
        marker = Marker(
            insert=(50, 50),
            viewBox="0 0 100 100",
            id_="FrozenThermometer-start",
            class_="FrozenThermometer FrozenThermometerStart"
        )
        marker.add(Circle(center=(50, 50), r=30))
        return marker

    def __repr__(self) -> str:
        """Return a string representation of the FrozenThermometerGlyph.

        Returns:
            str: A string representing the FrozenThermometerGlyph instance.
        """
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}]"
            f")"
        )
