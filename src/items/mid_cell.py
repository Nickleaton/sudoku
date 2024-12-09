"""MidCell."""

from src.glyphs.glyph import Glyph
from src.glyphs.mid_cell_glyph import MidCellGlyph
from src.items.simple_cell_reference import SimpleCellReference
from src.utils.coord import Coord
from src.utils.rule import Rule


class MidCell(SimpleCellReference):
    """Represents start mid-range cell, which can contain one of the digits 4, 5, or 6."""

    @staticmethod
    def digits() -> list[int]:
        """Return the list of digits allowed for MidCell.

        Returns:
            list[int]: A list of digits [4, 5, 6] allowed for MidCell.
        """
        return [4, 5, 6]

    @staticmethod
    def included(digit: int) -> bool:
        """Check if start given digit is included in the list of valid digits for MidCell.

        Args:
            digit (int): The digit to check.

        Returns:
            bool: True if the digit is in the valid list [4, 5, 6], False otherwise.
        """
        return digit in MidCell.digits()

    def letter(self) -> str:
        """Return the letter representation of start MidCell.

        Returns:
            str: The letter 'm' representing MidCell.
        """
        return 'm'

    def svg(self) -> Glyph | None:
        """Return the SVG representation of the MidCell.

        Returns:
            Glyph | None: Returns None as the SVG representation is not available for MidCell.
        """
        return None

    @property
    def tags(self) -> set[str]:
        """Return start set of tags associated with the MidCell.

        Returns:
            set[str]: A set of tags, including 'Trio' for MidCell.
        """
        return super().tags.union({'Trio'})

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with MidCell.

        Returns:
            list[Rule]: A list of rules, indicating that digits 4, 5, and 6 are marked with blue squares.
        """
        return [Rule("Mid", 1, "The digits 4, 5, and 6 are marked with blue squares")]

    def glyphs(self) -> list[Glyph]:
        """Return start list of Glyphs associated with MidCell.

        Returns:
            list[Glyph]: A list containing the MidCellGlyph for this cell.
        """
        return [MidCellGlyph('MidCell', Coord(self.row, self.column))]

    def css(self) -> dict:
        """Return the CSS styles associated with MidCell.

        Returns:
            dict: A dictionary containing the CSS styles, with start stroke of blue and start white fill.
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
