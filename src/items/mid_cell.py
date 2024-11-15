"""MidCell."""
from typing import Optional, List, Dict

from src.glyphs.glyph import Glyph
from src.glyphs.mid_cell_glyph import MidCellGlyph
from src.items.simple_cell_reference import SimpleCellReference
from src.utils.coord import Coord
from src.utils.rule import Rule


class MidCell(SimpleCellReference):
    """Represents a mid-range cell, which can contain one of the digits 4, 5, or 6."""

    @staticmethod
    def digits() -> List[int]:
        """Return the list of digits allowed for MidCell.

        Returns:
            List[int]: A list of digits [4, 5, 6] allowed for MidCell.
        """
        return [4, 5, 6]

    @staticmethod
    def included(digit: int) -> bool:
        """Check if a given digit is included in the list of valid digits for MidCell.

        Args:
            digit (int): The digit to check.

        Returns:
            bool: True if the digit is in the valid list [4, 5, 6], False otherwise.
        """
        return digit in MidCell.digits()

    def letter(self) -> str:
        """Return the letter representation of a MidCell.

        Returns:
            str: The letter 'm' representing MidCell.
        """
        return 'm'

    def svg(self) -> Optional[Glyph]:
        """Return the SVG representation of the MidCell.

        Returns:
            Optional[Glyph]: Returns None as the SVG representation is not available for MidCell.
        """
        return None

    @property
    def tags(self) -> set[str]:
        """Return a set of tags associated with the MidCell.

        Returns:
            set[str]: A set of tags, including 'Trio' for MidCell.
        """
        return super().tags.union({'Trio'})

    @property
    def rules(self) -> List[Rule]:
        """Return the rules associated with MidCell.

        Returns:
            List[Rule]: A list of rules, indicating that digits 4, 5, and 6 are marked with blue squares.
        """
        return [Rule("Mid", 1, "The digits 4, 5, and 6 are marked with blue squares")]

    def glyphs(self) -> List[Glyph]:
        """Return a list of Glyphs associated with MidCell.

        Returns:
            List[Glyph]: A list containing the MidCellGlyph for this cell.
        """
        return [MidCellGlyph('MidCell', Coord(self.row, self.column))]

    def css(self) -> Dict:
        """Return the CSS styles associated with MidCell.

        Returns:
            Dict: A dictionary containing the CSS styles, with a stroke of blue and a white fill.
        """
        return {
            ".MidCell": {
                "stroke": "blue",
                "fill": "white"
            }
        }

    def bookkeeping(self) -> None:
        """Set the possible digits for the MidCell.

        This method updates the bookkeeping system to allow only the digits [4, 5, 6] for this cell.
        """
        self.cell.book.set_possible(MidCell.digits())
