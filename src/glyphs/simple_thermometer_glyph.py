"""SimpleThermometerGlyph."""
from typing import Optional

from svgwrite.container import Marker
from svgwrite.shapes import Circle

from src.glyphs.thermometer_glyph import ThermometerGlyph


class SimpleThermometerGlyph(ThermometerGlyph):
    """A simple thermometer glyph with a custom start marker.

    This class extends ThermometerGlyph and adds a custom start marker
    and a string representation method to display essential attributes.
    """

    @classmethod
    def start_marker(cls) -> Optional[Marker]:
        """Create and return a custom marker for the start of the thermometer."""
        marker = Marker(
            insert=(50, 50),
            viewBox="0 0 100 100",
            id_="SimpleThermometer-start",
            class_="SimpleThermometer SimpleThermometerStart"
        )
        marker.add(Circle(center=(50, 50), r=30))
        return marker

    def __repr__(self) -> str:
        """Return a string representation of the SimpleThermometerGlyph."""
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}]"
            f")"
        )
