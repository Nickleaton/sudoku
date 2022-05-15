from typing import List, Dict

from src.items.special_region import SpecialRegion
from src.utils.coord import Coord


class Asterix(SpecialRegion):

    def coords(self) -> List[Coord]:
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
        return 'Asterix'

    def css(self) -> Dict:
        return {
            '.Asterix': {
                'stroke': 'orange',
                'fill': 'orange'
            }
        }
