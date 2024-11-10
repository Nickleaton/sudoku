from src.parsers.parser import Parser, ParserError
from src.tokens.digit_token import DigitToken
from src.tokens.side_token import SideToken
from src.tokens.symbols import EqualsToken
from src.tokens.value_token import ValueToken


class OutsideArrowValueParser(Parser):
    """Parser for Outside Arrow Value format: '[TLBR]d=d+'."""

    def __init__(self):
        """Initializes the OutsideArrowValueParser with a regex pattern for the Outside Arrow Value format."""
        super().__init__(pattern=r'^[TLBR]\d=\d+$', example_format="[TLBR]d=dd")
        self.token = SideToken() + DigitToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> None:
        """Parses the input text to extract components in the Outside Arrow Value format.

        Args:
            text (str): The input text expected to be in the format '[TLBR]d=d+'.

        Raises:
            ParserError: If the input text does not match the expected format.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects format like '[TLBR]d=d+'")

        try:
            stripped_text: str = text.replace(' ', '')
            lhs: str = stripped_text.split('=')[0]
            rhs: str = stripped_text.split('=')[1]
            side: str = lhs[0]  # 'T', 'L', 'B', or 'R'
            index: str = lhs[1]  # digit following the side
            value: str = rhs

            # Store results in the result attribute.
            self.result = [side, int(index), int(value)]
            self.answer = {
                'side': side,
                'index': index,
                'value': value,
            }
        except ValueError:
            self.raise_error()
