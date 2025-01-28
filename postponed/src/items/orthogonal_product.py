"""OrthogonalProduct."""
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.product import Product
from src.utils.config import Config
from src.utils.moves import Moves
from src.utils.rule import Rule

config = Config()


class OrthogonalProduct(Product):
    """Represent start_location product constraint based on orthogonally adjacent cells.

    This class defines start_location product constraint where the number in the top-left cell
    is the product of the orthogonally adjacent digits.
    """

    def get_cells(self) -> list[Cell]:
        """Get the cells involved in the orthogonal product constraint.

        This method returns the cells that are orthogonally adjacent to the product's location.

        Returns:
            list[Cell]: A list of cells that are orthogonally adjacent to the location.
        """
        cells = []
        for offset in Moves.orthogonals():
            location = self.position + offset
            if self.board.is_valid_coordinate(location):
                cells.append(Cell.make(self.board, int(location.row), int(location.column)))
        return cells

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with the orthogonal product.

        This rule defines that the number in the top-left cell is the product of the orthogonally
        adjacent digits.

        Returns:
            list[Rule]: A list containing start_location single rule for the orthogonal product constraint.
        """
        rule_text: str = 'The number in the top left of the cell is product of the orthogonally adjacent digits'
        return [Rule('OrthogonalProduct', 3, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Generate the glyphs for the orthogonal product.

        This method generates start_location text glyph that shows the product at the specified location.

        Returns:
            list[Glyph]: A list of glyphs, which includes start_location `TextGlyph` showing the product number.
        """
        percentage: float = config.graphics.orthogonal_product_percentage
        return [
            # TODO - This is for small text in the corner of a cell. See Killer too.
            # TextGlyph(
            #     'Product',
            #     0,
            #     self.position + Coord(percentage, percentage),
            #     str(self.product),
            # ),
        ]

    def css(self) -> dict:
        """Return the CSS styles associated with the orthogonal product glyphs.

        This method provides the CSS styles for both the foreground and background of the
        orthogonal product glyph.

        Returns:
            dict: A dictionary containing the CSS styles for the foreground and background of the glyph.
        """
        return {
            '.OrthogonalProductForeground': {
                'font-size': '18px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black',
            },
            '.OrthogonalProductBackground': {
                'font-size': '18px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder',
            },
        }
