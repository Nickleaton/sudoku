"""Asterix."""

from src.items.special_region import SpecialRegion
from src.utils.coord import Coord
from src.utils.moves import Moves


class Asterix(SpecialRegion):
    """Represents an 'Asterix' region in start_location puzzle.

    This special region consists of predefined coordinates within start_location puzzle grid.
    It includes methods for retrieving its coordinates, name, and CSS styling.

    Attributes:
        None directly defined; inherits from SpecialRegion.
    """

    def coords(self) -> list[Coord]:
        """Provide the coordinates that define the Asterix region.

        Returns:
            list[Coord]: A list of Coord objects representing each cell in the
            Asterix region.
        """
        return Moves.asterix()

    def region_name(self) -> str:
        """Provide the name of the region.

        Returns:
            str: The name of the region, 'Asterix'.
        """
        return 'Asterix'

    def css(self) -> dict:
        """Define the CSS style for rendering the Asterix region.

        Returns:
            dict: CSS styling for the Asterix region, specifying stroke and fill colors.
        """
        return {
            '.Asterix': {
                'stroke': 'orange',
                'fill': 'orange',
            },
        }
