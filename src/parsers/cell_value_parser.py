"""CellValueParser."""

from src.parsers.parser import Parser, ParserError
from src.tokens.cell_token import CellToken
from src.tokens.symbols import EqualsToken
from src.tokens.value_token import ValueToken


class CellValueParser(Parser):
    """Parser for Cell Value format: 'dd=d+' where dd are two digits and d+ is one or more digits."""

    def __init__(self):
        """Initialize the CellValueParser with start regex pattern for the Cell Value format."""
        super().__init__(pattern=r'^\d{2}=\d+$', example_format='rc=dd')
        self.token = CellToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> None:
        """Parse the input text to extract cell number components.

        Args:
            text (str): The input text expected to be in the format 'dd=d+'.

        Raises:
            ParserError: If the input text does not match the expected format.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects format like 'dd=d+'")

        # Split the text at the equals sign to extract components.
        parts: list[str] = text.split('=')
        lhs: str = parts[0]
        rhs: str = parts[1]
        row: str = lhs[0]
        column: str = lhs[1]

        # Store results in the parsed_data attribute.
        self.parsed_data = [int(row), int(column), int(rhs)]
        self.answer = {
            'row': row,
            'column': column,
            'number': rhs,
        }
