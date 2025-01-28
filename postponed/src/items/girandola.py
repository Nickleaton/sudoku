"""Girandola."""

from src.items.special_region import SpecialRegion
from src.utils.coord import Coord
from src.utils.moves import Moves


class Girandola(SpecialRegion):
    """Define the Girandola special region in the Sudoku grid."""

    def region_name(self) -> str:
        """Return the name of the region.

        Returns:
            str: The name of the region, 'Girandola'.
        """
        return 'Girandola'

    def coords(self) -> list[Coord]:
        """Return the coordinates that define the Girandola region.

        Returns:
            list[Coord]: A list of coordinates defining the Girandola region.
        """
        return Moves.girandola()

    def css(self) -> dict:
        """Return the CSS styling for the Girandola region.

        Returns:
            dict: A dictionary containing CSS properties for the 'Girandola' region.
        """
        return {
            '.Girandola': {
                'stroke': 'lightgreen',
                'fill': 'lightgreen',
            },
        }
