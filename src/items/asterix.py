"""Asterix."""
from typing import list, dict

from src.items.special_region import SpecialRegion
from src.utils.coord import Coord


class Asterix(SpecialRegion):
    """Represents an 'Asterix' region in a puzzle.

    This special region consists of predefined coordinates within a puzzle grid.
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
        return [
            Coord(2, 5),
            Coord(3, 3),
            Coord(3, 7),
            Coord(5, 2),
            Coord(5, 5),
            Coord(5, 8),
            Coord(7, 3),
            Coord(7, 7),
            Coord(8, 5)
        ]

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
                'fill': 'orange'
            }
        }
