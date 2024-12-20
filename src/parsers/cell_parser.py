"""CellParser."""
from src.parsers.parser import Parser, ParserError
from src.tokens.cell_token import CellToken


class CellParser(Parser):
    """Parser for a two-digit cell reference."""

    def __init__(self):
        """Initialize the CellParser with a regex pattern for two-digit numbers."""
        super().__init__(pattern=r"^\s*\d\d\s*$", example_format="rc")
        self.token = CellToken()

    def parse(self, text: str) -> None:
        """Parse the input text to extract two-digit cell references.

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
            stripped_text: str = text.strip()
            row: str = stripped_text[0]
            column: str = stripped_text[1]
            self.result = [int(row), int(column)]
            self.answer = {
                "row": row,
                "column": column
            }
        except ValueError:
            self.raise_error()
