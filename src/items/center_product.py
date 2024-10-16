from typing import List, Dict, Callable

from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.cell import Cell
from src.items.item import Item
from src.items.product import Product
from src.utils.coord import Coord
from src.utils.rule import Rule


class CenterProduct(Product):

    def get_cells(self) -> List[Cell]:
        offsets = [Coord(0, 0), Coord(0, 1), Coord(1, 0), Coord(1, 1)]
        cells = []
        for offset in offsets:
            location = self.position + offset
            if self.board.is_valid_coordinate(location):
                cells.append(Cell.make(self.board, int(location.row), int(location.column)))
        return cells

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule('CenterProduct', 3, 'The number is the product of the digits in the four surrounding cells')
        ]

    def glyphs(self) -> List[Glyph]:
        return [
            TextGlyph('CenterProduct', 0, self.position + Coord(1, 1), str(self.product))
        ]

    def css(self) -> Dict:
        return {
            '.CenterProductForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black'
            },
            '.CenterProductBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            }
        }
