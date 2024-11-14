from typing import List, Dict

from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.cell import Cell
from src.items.product import Product
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.rule import Rule


class CenterProduct(Product):
    """Represents a center product constraint in a Sudoku variant."""

    def get_cells(self) -> List[Cell]:
        """Retrieve the cells surrounding the center cell.

        Returns:
            List[Cell]: A list of four cells orthogonally adjacent to the center.
        """
        cells = []
        for offset in Direction.orthogonals():
            location = self.position + offset
            if self.board.is_valid_coordinate(location):
                cells.append(Cell.make(self.board, int(location.row), int(location.column)))
        return cells

    @property
    def rules(self) -> List[Rule]:
        """Define the rule associated with the center product.

        Returns:
            List[Rule]: A list containing the rule for center product.
        """
        return [
            Rule('CenterProduct', 3, 'The number is the product of the digits in the four surrounding cells')
        ]

    def glyphs(self) -> List[Glyph]:
        """Generate the glyphs for displaying the center product.

        Returns:
            List[Glyph]: A list containing the TextGlyph for the center product.
        """
        return [
            TextGlyph('CenterProduct', 0, self.position + Coord(1, 1), str(self.product))
        ]

    def css(self) -> Dict:
        """Return the CSS styling for the center product glyphs.

        Returns:
            Dict: A dictionary containing CSS styles for foreground and background.
        """
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
