from typing import List, Dict, Callable

from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.cell import Cell
from src.items.item import Item
from src.items.product import Product
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.rule import Rule


class OrthogonalProduct(Product):

    def get_cells(self) -> List[Cell]:
        cells = []
        for offset in Direction.orthogonals():
            location = self.position + offset
            if self.board.is_valid_coordinate(location):
                cells.append(Cell.make(self.board, int(location.row), int(location.column)))
        return cells

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule('OrthogonalProduct', 3,
                 'The number in the top left of the cell is product of the orthoganally adjacent digits')
        ]

    def glyphs(self) -> List[Glyph]:
        return [
            TextGlyph('Product', 0, self.position + Coord(0.15, 0.15), str(self.product))
        ]

    def css(self) -> Dict:
        return {
            '.OrthogonalProductForeground': {
                'font-size': '18px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black'
            },
            '.OrthogonalProductBackground': {
                'font-size': '18px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            }
        }
