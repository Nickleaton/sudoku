"""DigitsParser."""
from src.parsers.parser import Parser, ParserError
from src.tokens.digit_token import DigitToken
from src.tokens.symbols import CommaToken
from src.tokens.token import Token


class DigitsParser(Parser):
    """Parse a comma-separated list of single digits from a string.

    Attributes:
        result (list[int]): A list of parsed integer digits from the input string.
    """

    def __init__(self):
        """Initialize DigitsParser with a regex pattern for comma-separated digits."""
        super().__init__(pattern=r"^\d(?:,\d)*$", example_format="1,2,3,...")
        self.token: Token = DigitToken() + (CommaToken() + DigitToken()) * (0, 999)

    def parse(self, text: str) -> None:
        """Parse a comma-separated string of digits.

        This method input_types if the provided input string matches the expected
        pattern of a comma-separated list of digits. If the input is valid,
        it processes the string to extract the digits and stores them in
        the result attribute as a list of integers.

        Args:
            text (str): The input string to parse.

        Raises:
            ParserError: If the input does not match the expected format or
                         if any of the parsed values cannot be converted to
                         an integer.
        """
        # Check if the input text matches the defined regular expression pattern
        text = text.replace(" ", "")
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects a comma-separated list of digits")

        try:
            # Split the input text by commas, strip whitespace from each digit,
            # and convert them to integers. The result is stored in the result attribute.
            self.result = [int(d.strip()) for d in text.split(',')]
            self.answer = [d.strip() for d in text.split(',')]
        except ValueError:
            self.raise_error()
