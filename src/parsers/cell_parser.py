from src.parsers.parser import Parser, ParserError


class CellParser(Parser):
    """Parser for a two-digit cell reference."""

    def __init__(self):
        """Initializes the CellParser with a regex pattern for two-digit numbers."""
        super().__init__(r"^\s*\d\d\s*$")

    def parse(self, text: str) -> None:
        """Parses the input text to extract two-digit cell references.

        Args:
            text (str): The input text expected to be a two-digit cell reference.

        Raises:
            ParserError: If the input text does not match the expected format
                          or if conversion to integers fails.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects a two digit cell reference")

        try:
            # Strip whitespace and convert the first two characters to integers,
            # storing the result as a list of integers in the result attribute.
            self.result = [int(text.strip()[0]), int(text.strip()[1])]
        except ValueError:
            # If any of the values cannot be converted to an integer, clear the result and raise an error.
            self.result = None
            raise ParserError(f"{self.__class__.__name__} expects a two digit cell reference")
