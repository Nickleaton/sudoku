"""OrthogonalProduct."""
from typing import List, Dict

from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.cell import Cell
from src.items.product import Product
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.rule import Rule


class OrthogonalProduct(Product):
    """Represent a product constraint based on orthogonally adjacent cells.

    This class defines a product constraint where the number in the top-left cell
    is the product of the orthogonally adjacent digits.
    """

    def get_cells(self) -> List[Cell]:
        """Get the cells involved in the orthogonal product constraint.

        This method returns the cells that are orthogonally adjacent to the product's position.

        Returns:
            List[Cell]: A list of cells that are orthogonally adjacent to the position.
        """
        cells = []
        for offset in Direction.orthogonals():
            location = self.position + offset
            if self.board.is_valid_coordinate(location):
                cells.append(Cell.make(self.board, int(location.row), int(location.column)))
        return cells

    @property
    def rules(self) -> List[Rule]:
        """Return the rules associated with the orthogonal product.

        This rule defines that the number in the top-left cell is the product of the orthogonally
        adjacent digits.

        Returns:
            List[Rule]: A list containing a single rule for the orthogonal product constraint.
        """
        return [
            Rule('OrthogonalProduct', 3,
                 'The number in the top left of the cell is product of the orthogonally adjacent digits')
        ]

    def glyphs(self) -> List[Glyph]:
        """Generate the glyphs for the orthogonal product.

        This method generates a text glyph that shows the product at the specified position.

        Returns:
            List[Glyph]: A list of glyphs, which includes a `TextGlyph` showing the product value.
        """
        return [
            TextGlyph('Product', 0, self.position + Coord(0.15, 0.15), str(self.product))
        ]

    def css(self) -> Dict:
        """Return the CSS styles associated with the orthogonal product glyphs.

        This method provides the CSS styles for both the foreground and background of the
        orthogonal product glyph.

        Returns:
            Dict: A dictionary containing the CSS styles for the foreground and background of the glyph.
        """
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
