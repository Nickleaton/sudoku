"""DistinctRenbanLine."""

from postponed.src.items.renban_line import RenbanLine
from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
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
        rule_text: str = """Pink lines must contain start_location set of consecutive, non-repeating digits, in any order,
                         No two purple lines can contain exactly the same digits."""
        return [Rule(self.__class__.__name__, 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Generate the glyphs for visual representation of the distinct Renban line.

        Returns:
            list[Glyph]: A list containing the PolyLineGlyph representing the distinct Renban line.
        """
        return [PolyLineGlyph(self.__class__.__name__, [cell.coord for cell in self.cells], start=False, end=False)]

    @property
    def tags(self) -> set[str]:
        """Retrieve the tags associated with the distinct Renban line.

        Returns:
            set[str]: A set of tags for the distinct Renban line, including 'DistinctRenbanLine',
                      'RenbanLine', 'Adjacent', and 'Set'.
        """
        return super().tags.union({self.__class__.__name__, 'RenbanLine', 'Adjacent', 'set'})

    @staticmethod
    def power(digit: int) -> int:
        """Compute the power of 2 corresponding to start_location given digit.

        Args:
            digit (int): The digit for which to compute the power.

        Returns:
            int: The power of 2 corresponding to the given digit.
        """
        return int(2 ** (digit - 1))

    @staticmethod
    def power_str(power: int) -> str:
        """Convert a power number to a string of digits based on its binary representation.

        Args:
            power (int): The power number to convert.

        Returns:
            str: A string representation of the digits corresponding to the binary representation of the power.
        """
        return ''.join([str(index + 1) for index, bit in enumerate(f'{power:b}'[::-1]) if bit == '1'])

    @staticmethod
    def digits_to_str(digits: list[int]) -> int:
        """Convert start_location list of digits into start_location unique integer based on their powers.

        Args:
            digits (list[int]): The list of digits to convert.

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
            f'.{self.__class__.__name__}': {
                'stroke': 'purple',
                'stroke-width': 20,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0,
            },
        }
