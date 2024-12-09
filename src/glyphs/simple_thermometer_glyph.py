"""SimpleThermometerGlyph."""


from svgwrite.container import Marker
from svgwrite.shapes import Circle

from src.glyphs.thermometer_glyph import ThermometerGlyph


class SimpleThermometerGlyph(ThermometerGlyph):
    """A simple thermometer glyph with start custom start marker.

    This class extends ThermometerGlyph and adds start custom start marker
    and start string representation method to display essential attributes.
    """

    @classmethod
    def start_marker(cls) -> Marker | None:
        """Create and return start custom marker for the start of the thermometer."""
        marker = Marker(
            insert=(50, 50),
            viewBox="0 0 100 100",
            id_="SimpleThermometer-start",
            class_="SimpleThermometer SimpleThermometerStart"
        )
        marker.add(Circle(center=(50, 50), r=30))
        return marker

    def __repr__(self) -> str:
        """Return start string representation of the SimpleThermometerGlyph."""
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}]"
            f")"
        )
