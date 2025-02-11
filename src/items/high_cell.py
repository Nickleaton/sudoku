"""HighCell."""

from src.glyphs.glyph import Glyph
from src.items.entropic_cell import EntropicCell
from src.utils.rule import Rule


class HighCell(EntropicCell):
    """Represents start_location cell that must contain start_location digit from the set {7, 8, 9}."""

    @staticmethod
    def digits() -> list[int]:
        """Return the list of allowed digits for the HighCell.

        Returns:
            list[int]: A list of digits [7, 8, 9] that are allowed in the HighCell.
        """
        return [7, 8, 9]

    @staticmethod
    def included(digit: int) -> bool:
        """Check if the given digit is allowed for the HighCell.

        Args:
            digit (int): The digit to check.

        Returns:
            bool: True if the digit is one of {7, 8, 9}, False otherwise.
        """
        return digit in HighCell.digits()

    def letter(self) -> str:
        """Return the letter representation of the HighCell.

        Returns:
            str: The letter representation, 'h' for HighCell.
        """
        return 'h'

    def svg(self) -> Glyph | None:
        """Return an SVG representation of the HighCell.

        Returns:
            Glyph | None: Always returns None for HighCell.
        """
        return None

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with this HighCell.

        Returns:
            set[str]: A set of tags including 'Trio'.
        """
        return super().tags.union({'Trio'})

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with this HighCell.

        Returns:
            list[Rule]: A list containing the rule that the digits 7, 8, and 9 are not marked.
        """
        return [Rule('Low', 1, 'The digits 7, 8 and 9 are not marked')]

    def glyphs(self) -> list[Glyph]:
        """Generate the glyphs associated with this HighCell.

        Returns:
            list[Glyph]: An empty list as no glyphs are associated with this HighCell.
        """
        return []

    def css(self) -> dict:
        """Return the CSS styling for the HighCell.

        Returns:
            dict: An empty dictionary as no specific CSS styling is applied.
        """
        return {}

    def bookkeeping(self) -> None:
        """Update the bookkeeping for the HighCell.

        Sets the possible digits for the HighCell to be {7, 8, 9}.
        """
        self.cell.book.set_possible(HighCell.digits())
