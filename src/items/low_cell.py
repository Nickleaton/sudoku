"""LowCell."""
from typing import Optional, List, Dict

from src.glyphs.glyph import Glyph
from src.glyphs.low_cell_glyph import LowCellGlyph
from src.items.simple_cell_reference import SimpleCellReference
from src.utils.coord import Coord
from src.utils.rule import Rule


class LowCell(SimpleCellReference):
    """Represents a low cell, which can contain one of the digits 1, 2, or 3."""

    @staticmethod
    def digits() -> List[int]:
        """Return the list of digits allowed for LowCell.

        Returns:
            List[int]: A list of digits [1, 2, 3] allowed for LowCell.
        """
        return [1, 2, 3]

    @staticmethod
    def included(digit: int) -> bool:
        """Check if a given digit is included in the list of valid digits for LowCell.

        Args:
            digit (int): The digit to check.

        Returns:
            bool: True if the digit is in the valid list [1, 2, 3], False otherwise.
        """
        return digit in LowCell.digits()

    def letter(self) -> str:
        """Return the letter representation of a LowCell.

        Returns:
            str: The letter 'l' representing LowCell.
        """
        return 'l'

    def svg(self) -> Optional[Glyph]:
        """Return the SVG representation of the LowCell.

        Returns:
            Optional[Glyph]: Returns None as the SVG representation is not available for LowCell.
        """
        return None

    @property
    def tags(self) -> set[str]:
        """Return a set of tags associated with the LowCell.

        Returns:
            set[str]: A set of tags, including 'Trio' for LowCell.
        """
        return super().tags.union({'Trio'})

    @property
    def rules(self) -> List[Rule]:
        """Return the rules associated with LowCell.

        Returns:
            List[Rule]: A list of rules, indicating that digits 1, 2, and 3 are marked with orange circles.
        """
        return [Rule("Low", 1, "The digits 1, 2, and 3 are marked with orange circles")]

    def glyphs(self) -> List[Glyph]:
        """Return a list of Glyphs associated with LowCell.

        Returns:
            List[Glyph]: A list containing the LowCellGlyph for this cell.
        """
        return [LowCellGlyph('LowCell', Coord(self.row, self.column))]

    def css(self) -> Dict:
        """Return the CSS styles associated with LowCell.

        Returns:
            Dict: A dictionary containing the CSS styles, with a stroke of orange and a white fill.
        """
        return {
            ".LowCell": {
                "stroke": "orange",
                "fill": "white"
            }
        }

    def bookkeeping(self) -> None:
        """Set the possible digits for the LowCell.

        This method updates the bookkeeping system to allow only the digits [1, 2, 3] for this cell.
        """
        self.cell.book.set_possible(LowCell.digits())

