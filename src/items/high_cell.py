from typing import Optional, List, Dict

# from src.glyphs.glyph import Glyph, HighCellGlyph
from src.glyphs.glyph import Glyph
from src.items.simple_cell_reference import SimpleCellReference
from src.utils.rule import Rule


class HighCell(SimpleCellReference):
    """Represents a cell that must contain a digit from the set {7, 8, 9}."""

    @staticmethod
    def digits() -> List[int]:
        """Returns the list of allowed digits for the HighCell.

        Returns:
            List[int]: A list of digits [7, 8, 9] that are allowed in the HighCell.
        """
        return [7, 8, 9]

    @staticmethod
    def included(digit: int) -> bool:
        """Checks if the given digit is allowed for the HighCell.

        Args:
            digit (int): The digit to check.

        Returns:
            bool: True if the digit is one of {7, 8, 9}, False otherwise.
        """
        return digit in HighCell.digits()

    def letter(self) -> str:
        """Returns the letter representation of the HighCell.

        Returns:
            str: The letter representation, 'h' for HighCell.
        """
        return 'h'

    def svg(self) -> Optional[Glyph]:
        """Returns an SVG representation of the HighCell.

        Returns:
            Optional[Glyph]: Always returns None for HighCell.
        """
        return None

    @property
    def tags(self) -> set[str]:
        """Returns the tags associated with this HighCell.

        Returns:
            set[str]: A set of tags including 'Trio'.
        """
        return super().tags.union({'Trio'})

    @property
    def rules(self) -> List[Rule]:
        """Returns the rules associated with this HighCell.

        Returns:
            List[Rule]: A list containing the rule that the digits 7, 8, and 9 are not marked.
        """
        return [Rule("Low", 1, "The digits 7, 8 and 9 are not marked")]

    def glyphs(self) -> List[Glyph]:
        """Generates the glyphs associated with this HighCell.

        Returns:
            List[Glyph]: An empty list as no glyphs are associated with this HighCell.
        """
        return []
        # return [HighCellGlyph('HighCell', Coord(self.row, self.column))]

    def css(self) -> Dict:
        """Returns the CSS styling for the HighCell.

        Returns:
            Dict: An empty dictionary as no specific CSS styling is applied.
        """
        return {}

    def bookkeeping(self) -> None:
        """Updates the bookkeeping for the HighCell.

        Sets the possible digits for the HighCell to be {7, 8, 9}.
        """
        self.cell.book.set_possible(HighCell.digits())
