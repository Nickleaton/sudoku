from typing import List, Optional

from src.parsers.parser import Parser, ParserError


class DigitsParser(Parser):
    """Parses a comma-separated list of single digits from a string.

    Attributes:
        result (list[int]): A list of parsed integer digits from the input string.
    """

    def __init__(self):
        """Initializes DigitsParser with a regex pattern for comma-separated digits."""
        super().__init__(r"^\s*\d\s*(?:,\s*\d\s*)*$")
        self.answer: Optional[List[int]] = None

    def parse(self, text: str) -> None:
        """Parses a comma-separated string of digits.

        This method checks if the provided input string matches the expected
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
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects a comma-separated list of digits")

        try:
            # Split the input text by commas, strip whitespace from each digit,
            # and convert them to integers. The result is stored in the result attribute.
            self.result = [int(d.strip()) for d in text.split(',')]
            self.answer = [d.strip() for d in text.split(',')]
        except ValueError:
            # Raise an error if any of the values cannot be converted to an integer
            self.result = None
            raise ParserError(f"{self.__class__.__name__} expects a comma-separated list of digits")
