from typing import List

from src.glyphs.glyph import Glyph, TextGlyph
from src.items.cell import Cell
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
                cells.append(Cell.make(self.board, location.row, location.column))
        return cells

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule('CenterProduct', 3, 'The number is the product of the digits in the four surronding cells')
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [
            TextGlyph('CenterProduct', 0, self.position + Coord(1, 1), str(self.product))
        ]
