from src.parsers.parser import Parser, ParserError


class CellListParser(Parser):
    """Parser for a comma-separated list of cell coordinates."""

    def __init__(self):
        """Initialize the CellListParser with a specific regex pattern."""
        super().__init__(r"^\s*\d\d\s*(?:,\s*\d\d\s*)*$")

    def parse(self, text: str) -> None:
        """Parse the input text into a list of cell coordinates.

        Args:
            text (str): The input string containing comma-separated cell coordinates.

        Raises:
            ParserError: If the input does not match the expected format or if
                         any coordinates cannot be converted to integers.
        """
        # Check if the input text matches the defined regular expression pattern
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects a comma-separated list of cell coordinates")

        try:
            # Split the input text by commas, strip whitespace, and convert each
            # coordinate into a list of integers. The result is stored in the result attribute.
            self.result = [[int(d.strip()[0]), int(d.strip()[1])] for d in text.split(',')]
        except ValueError:
            # Raise an error if any of the values cannot be converted to integers
            self.result = None
            raise ParserError(f"{self.__class__.__name__} expects a comma-separated list of cell coordinates")
