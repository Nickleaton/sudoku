"""RossiniParser."""
from src.parsers.parser import Parser, ParserError
from src.tokens.digit_token import DigitToken
from src.tokens.direction_token import DirectionToken
from src.tokens.side_token import SideToken
from src.tokens.symbols import EqualsToken


class RossiniParser(Parser):
    """Parser for Rossini format: '[TLBR]d=[DIU]'."""

    def __init__(self):
        """Initialize the RossiniParser with a regex pattern for the Rossini format."""
        super().__init__(pattern=r'^[TLBR]\d=[DIU]$', example_format="[TLBR]d=[DIU]")
        self.token = SideToken() + DigitToken() + EqualsToken() + DirectionToken()

    def parse(self, text: str) -> None:
        """Parse the input text to extract components in the Rossini format.

        Args:
            text (str): The input text expected to be in the format '[TLBR]d=[DIU]'.

        Raises:
            ParserError: If the input text does not match the expected format.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects format like '[TLBR]d=[DIU]'")

        try:

            # Extract the components: side, index, and direction.
            side = text[0]  # 'T', 'L', 'B', or 'R'
            index = int(text[1])  # digit following the side
            direction = text[3]  # 'D', 'I', or 'U'

            # Store results in the result attribute.
            self.result = [side, index, direction]
            self.answer = {
                'side': side,
                'index': str(index),
                'direction': direction
            }

        except ValueError:
            self.raise_error()
