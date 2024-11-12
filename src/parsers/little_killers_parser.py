"""LittleKillersParser."""
from src.parsers.parser import Parser, ParserError
from src.tokens.digit_token import DigitToken
from src.tokens.direction_token import DirectionToken
from src.tokens.side_token import SideToken
from src.tokens.symbols import EqualsToken
from src.tokens.value_token import ValueToken


class LittleKillersParser(Parser):
    """Parser for the Little Killers format."""

    def __init__(self):
        """Initialize the LittleKillersParser with a regex pattern for valid input formats."""
        super().__init__(pattern=r"^\s*[TLBR]\s*\d\s*[C|A]\s*=\s*\d+\s*$", example_format="[TLBR]i=dd")
        self.token = SideToken() + DigitToken() + DirectionToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> None:
        """Parse the input text to extract components of the Little Killers format.

        Args:
            text (str): The input text expected to be in the format 'T1C=2' or similar.

            First letter is T, L, B, or R corresponding to the side of the board, Top, Left, Right or Bottom.
            Second number is the index of the cell. Column or row index
            Third letter is C or A corresponding to the direction of the cell, Clockwise or Anticlockwise.
            Last number is the value depending on the constraint

        Raises:
            ParserError: If the input text does not match the expected format
                          or if conversion to integers fails.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects input in the format 'T1C=2' or similar")

        try:
            # Remove whitespace from the input text.
            stripped_text: str = text.replace(" ", "")

            # Extract the components based on the specified format.
            side: str = stripped_text[0]  # The first character (T, L, B, R)
            index: str = stripped_text[1]  # The second character as an integer index
            direction: str = stripped_text[2]  # The third character (C or A)
            value: str = stripped_text.split("=")[1]  # The value after '='

            # Store the extracted components in the result attribute.
            self.result = [side, int(index), direction, int(value)]
            self.answer = {
                'side': side,
                'index': index,
                'direction': direction,
                'value': value
            }
        except ValueError:
            self.raise_error()
