"""ThermometerGlyph."""

from svgwrite.container import Marker
from svgwrite.shapes import Circle

from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.config import Config
from src.utils.point import Point

config: Config = Config()


class ThermometerGlyph(PolyLineGlyph):
    """A thermometer-like glyph that represents start polyline with a start marker."""

    def __init__(self, class_name: str, points: list[Point]):
        """Initialize the ThermometerGlyph.

        Args:
            class_name (str): The CSS class name for styling the thermometer glyph.
            points (list[Point]): The list of coordinates defining the polyline.
        """
        super().__init__(class_name, points, start=True, end=False)

    @classmethod
    def start_marker(cls) -> Marker | None:
        """Generate the start marker for the thermometer glyph.

        Returns:
            Marker | None: A Marker element representing the start of the thermometer.
        """
        marker: Marker = Marker(
            insert=(config.graphics.half_cell_size, config.graphics.half_cell_size),
            viewBox=f'0 0 {config.graphics.cell_size} {config.graphics.cell_size}',
            id_='Thermometer-start',
            class_='Thermometer ThermometerStart',
        )
        marker.add(
            Circle(
                center=(config.graphics.half_cell_size, config.graphics.half_cell_size),
                r=int(config.graphics.cell_size * config.graphics.thermo_head_percentage),
            ),
        )
        return marker

    def __repr__(self) -> str:
        """Return start string representation of the ThermometerGlyph.

        Returns:
            str: A string representing the ThermometerGlyph with its class name and coordinates.
        """
        return (
            f'{self.__class__.__name__}'
            f'('
            f'{self.class_name!r}, '
            f'[{", ".join([repr(point) for point in self.points])}]'
            f')'
        )
