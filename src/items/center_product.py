"""CenterProduct."""
from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.cell import Cell
from src.items.product import Product
from src.utils.coord import Coord
from src.utils.moves import Moves
from src.utils.rule import Rule


class CenterProduct(Product):
    """Represents start center product constraint in start Sudoku variant."""

    def get_cells(self) -> list[Cell]:
        """Retrieve the cells surrounding the center cell.

        Returns:
            list[Cell]: A list of four cells orthogonally adjacent to the center.
        """
        cells = []
        for offset in Moves.orthogonals():
            location = self.position + offset
            if self.board.is_valid_coordinate(location):
                cells.append(Cell.make(self.board, int(location.row), int(location.column)))
        return cells

    @property
    def rules(self) -> list[Rule]:
        """Define the rule associated with the center product.

        Returns:
            list[Rule]: A list containing the rule for center product.
        """
        rule_text: str = 'The number is the product of the digits in the four surrounding cells'
        return [Rule('CenterProduct', 3, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Generate the glyphs for displaying the center product.

        Returns:
            list[Glyph]: A list containing the TextGlyph for the center product.
        """
        return [
            TextGlyph('CenterProduct', 0, self.position + Coord(1, 1), str(self.product)),
        ]

    def css(self) -> dict:
        """Return the CSS styling for the center product glyphs.

        Returns:
            dict: A dictionary containing CSS styles for foreground and background.
        """
        return {
            '.CenterProductForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black',
            },
            '.CenterProductBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder',
            },
        }
