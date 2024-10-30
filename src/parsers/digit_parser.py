from typing import Dict, Optional

from src.parsers.parser import Parser, ParserError


class DigitParser(Parser):
    """Parser for a single digit."""

    def __init__(self):
        """Initializes the DigitParser with a regex pattern for a one-digit number."""
        super().__init__(r"^\s*\d\s*$")
        self.answer: Optional[Dict[str, int]] = None

    def parse(self, text: str) -> None:
        """Parses the input text to extract a single digit.

        Args:
            text (str): The input text expected to be a single digit.

        Raises:
            ParserError: If the input text does not match the expected format
                          or if conversion to an integer fails.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects one digit")

        try:
            # Strip whitespace and convert the first character to an integer,
            # storing the result directly in the result attribute.
            self.result = int(text.strip()[0])
            self.answer = {'digit': text.strip()[0]}
        except ValueError:
            # If the value cannot be converted to an integer, clear the result and raise an error.
            self.result = None
            raise ParserError(f"{self.__class__.__name__} expects one digit")
