"""EvenCell."""
from typing import Optional, List, Dict

from src.glyphs.even_cell_glyph import EvenCellGlyph
from src.glyphs.glyph import Glyph
from src.items.simple_cell_reference import SimpleCellReference
from src.utils.coord import Coord
from src.utils.rule import Rule


class EvenCell(SimpleCellReference):
    """Represents a cell that must contain an even digit."""

    @staticmethod
    def included(digit: int) -> bool:
        """Check if the digit is even.

        Args:
            digit (int): The digit to check.

        Returns:
            bool: True if the digit is even, False otherwise.
        """
        return digit % 2 == 0

    def letter(self) -> str:
        """Return the letter representation of the EvenCell.

        Returns:
            str: The letter representation, 'e' for EvenCell.
        """
        return 'e'

    def svg(self) -> Optional[Glyph]:
        """Return an SVG representation of the EvenCell.

        Returns:
            Optional[Glyph]: Always returns None for EvenCell.
        """
        return None

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with this EvenCell.

        Returns:
            set[str]: A set of tags including 'Parity'.
        """
        return super().tags.union({'Parity'})

    @property
    def rules(self) -> List[Rule]:
        """Return the rules associated with this EvenCell.

        Returns:
            List[Rule]: A list containing the rule that specifies an opaque grey square must contain an even digit.
        """
        return [Rule("Odd", 1, "An opaque grey square must contain an even digit")]

    def glyphs(self) -> List[Glyph]:
        """Generate the glyphs associated with this EvenCell.

        Returns:
            List[Glyph]: A list containing the EvenCellGlyph.
        """
        return [EvenCellGlyph('EvenCell', Coord(self.row, self.column))]

    def css(self) -> Dict:
        """Return the CSS styling for the EvenCell.

        Returns:
            Dict: A dictionary containing the CSS properties for the EvenCell.
        """
        return {
            ".EvenCell": {
                "fill": "gainsboro"
            }
        }

    def bookkeeping(self) -> None:
        """Update the bookkeeping for the EvenCell.

        Sets the impossibility of containing odd digits in the cell's bookkeeping.
        """
        self.cell.book.set_impossible([digit for digit in self.board.digit_range if not EvenCell.included(digit)])
