"""OddCell."""

from src.glyphs.glyph import Glyph
from src.glyphs.odd_cell_glyph import OddCellGlyph
from src.items.simple_cell_reference import SimpleCellReference
from src.utils.coord import Coord
from src.utils.rule import Rule


class OddCell(SimpleCellReference):
    """Represents an odd-numbered cell, which must contain an odd digit."""

    @staticmethod
    def included(digit: int) -> bool:
        """Check if the given digit is odd and valid for OddCell.

        Args:
            digit (int): The digit to check.

        Returns:
            bool: True if the digit is odd, False otherwise.
        """
        return digit % 2 == 1

    def svg(self) -> Glyph | None:
        """Return the SVG representation of the OddCell.

        Returns:
            Glyph | None: Returns None as the SVG representation is not available for OddCell.
        """
        return None

    def letter(self) -> str:
        """Return the letter representation of an OddCell.

        Returns:
            str: The letter 'o' representing OddCell.
        """
        return 'o'

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with OddCell.

        Returns:
            list[Rule]: A list of rules, indicating that an opaque grey circle must contain an odd digit.
        """
        return [Rule("Odd", 1, "An opaque grey circle must contain an odd digit")]

    def glyphs(self) -> list[Glyph]:
        """Return a list of Glyphs associated with OddCell.

        Returns:
            list[Glyph]: A list containing the OddCellGlyph for this cell.
        """
        return [OddCellGlyph('OddCell', Coord(self.row, self.column))]

    @property
    def tags(self) -> set[str]:
        """Return a set of tags associated with OddCell.

        Returns:
            set[str]: A set of tags, including 'Parity' for OddCell.
        """
        return super().tags.union({'Parity'})

    def css(self) -> dict:
        """Return the CSS styles associated with OddCell.

        Returns:
            dict: A dictionary containing the CSS styles, with a fill color of 'gainsboro' for OddCell.
        """
        return {
            ".OddCell": {
                "fill": "gainsboro"
            }
        }

    def bookkeeping(self) -> None:
        """Set the impossible digits for the OddCell.

        This method updates the bookkeeping system to exclude even digits and allow only odd digits for this cell.
        """
        self.cell.book.set_impossible([digit for digit in self.board.digit_range if not OddCell.included(digit)])
