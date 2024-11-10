from typing import List

from src.parsers.parser import Parser, ParserError
from src.tokens.cell_token import CellToken
from src.tokens.symbols import EqualsToken
from src.tokens.value_token import ValueToken


class CellValueParser(Parser):
    """Parser for Cell Value format: 'dd=d+' where dd are two digits and d+ is one or more digits."""

    def __init__(self):
        """Initializes the CellValueParser with a regex pattern for the Cell Value format."""
        super().__init__(pattern=r'^\d{2}=\d+$', example_format='rc=dd')
        self.token = CellToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> None:
        """Parses the input text to extract cell value components.

        Args:
            text (str): The input text expected to be in the format 'dd=d+'.

        Raises:
            ParserError: If the input text does not match the expected format.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects format like 'dd=d+'")

        try:
            # Split the text at the equals sign to extract components.
            parts: List[str] = text.split('=')
            lhs: str = parts[0]
            rhs: str = parts[1]
            row: str = lhs[0]
            column: str = lhs[1]
            value: str = rhs

            # Store results in the result attribute.
            self.result = [int(row), int(column), int(value)]
            self.answer = {
                'row': row,
                'column': column,
                'value': value
            }
        except ValueError:
            self.raise_error()
