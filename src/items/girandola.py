from typing import List, Dict

from src.items.special_region import SpecialRegion
from src.utils.coord import Coord


class Girandola(SpecialRegion):

    def region_name(self) -> str:
        return "Girandola"

    def coords(self) -> List[Coord]:
        return [
            Coord(1, 1),
            Coord(1, 9),
            Coord(2, 5),
            Coord(5, 2),
            Coord(5, 5),
            Coord(5, 8),
            Coord(8, 5),
            Coord(9, 1),
            Coord(9, 9)
        ]

    def css(self) -> Dict:
        return {
            ".Girandola": {
                "stroke": "lightgreen",
                "fill": "lightgreen"
            }
        }
