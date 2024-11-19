"""DistinctRenbanLine."""
from typing import list, dict

from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.renban_line import RenbanLine
from src.utils.rule import Rule


class DistinctRenbanLine(RenbanLine):
    """Distinct Renban line.

    The digits on the line are consecutive,non-repeating.
    No two lines contain exactly the same set of digits.
    """

    @property
    def rules(self) -> list[Rule]:
        """Retrieve the rules for the distinct Renban line.

        Returns:
            list[Rule]: A list of rules for the distinct Renban line.
        """
        return [
            Rule(
                'DistinctRenbanLine',
                1,
                "Pink lines must contain a set of consecutive, non-repeating digits, in any order,"
                " No two purple lines can contain exactly the same digits"
            )
        ]

    def glyphs(self) -> list[Glyph]:
        """Generate the glyphs for visual representation of the distinct Renban line.

        Returns:
            list[Glyph]: A list containing the PolyLineGlyph representing the distinct Renban line.
        """
        return [PolyLineGlyph('DistinctRenbanLine', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        """Retrieve the tags associated with the distinct Renban line.

        Returns:
            set[str]: A set of tags for the distinct Renban line, including 'DistinctRenbanLine',
                      'RenbanLine', 'Adjacent', and 'Set'.
        """
        return super().tags.union({'DistinctRenbanLine', 'RenbanLine', 'Adjacent', 'set'})

    @staticmethod
    def power(digit: int) -> int:
        """Compute the power of 2 corresponding to a given digit.

        Args:
            digit (int): The digit for which to compute the power.

        Returns:
            int: The power of 2 corresponding to the given digit.
        """
        return 2 ** (digit - 1)

    @staticmethod
    def power_str(power: int) -> str:
        """Convert a power value to a string of digits based on its binary representation.

        Args:
            power (int): The power value to convert.

        Returns:
            str: A string representation of the digits corresponding to the binary representation of the power.
        """
        return "".join([str(i + 1) for i, c in enumerate(f"{power:b}"[::-1]) if c == '1'])

    @staticmethod
    def digits_to_str(digits: list[int]) -> int:
        """Convert a list of digits into a unique integer based on their powers.

        Args:
            digits (List[int]): The list of digits to convert.

        Returns:
            int: A unique integer representing the sum of the powers of the digits.
        """
        return sum([DistinctRenbanLine.power(digit) for digit in digits])

    def css(self) -> dict:
        """Retrieve the CSS style for rendering the distinct Renban line.

        Returns:
            dict: A dictionary containing the CSS properties for the distinct Renban line.
        """
        return {
            '.DistinctRenbanLine': {
                'stroke': 'purple',
                'stroke-width': 20,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0
            }
        }
