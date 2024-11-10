from typing import List

from src.parsers.parser import Parser, ParserError
from src.tokens.cell_token import CellToken
from src.tokens.digit_token import DigitToken
from src.tokens.symbols import EqualsToken, QuestionMarkToken


class QuadruplesParser(Parser):
    """Parser for quadruples in the format 'dd=ddd' where d is a digit and '?' is allowed."""

    def __init__(self):
        """Initializes the QuadruplesParser with a regex pattern for the quadruples format."""
        super().__init__(pattern=r'^\d{2}=[\d?]+$', example_format='rc=dd??')
        self.token = CellToken() + EqualsToken() + (DigitToken() + QuestionMarkToken()) * (1,4)

    def parse(self, text: str) -> None:
        """Parses the input text to extract quadruple components.

        Args:
            text (str): The input text expected to be in the format 'dd=ddd'.

        Raises:
            ParserError: If the input text does not match the expected format
                          or if conversion to integers fails.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects a format like 'dd=ddd'")

        try:
            # Split the input string into components based on '='
            stripped_text: str = text.replace(" ", "")
            lhs: str = stripped_text.split('=')[0]
            rhs: str = stripped_text.split('=')[1]

            row: str = lhs[0]
            column: str = lhs[1]
            choices: List[str] = list(rhs)
            # Store results: left should be two digits, right can be digits or '?'.
            self.result = [int(row), int(column), rhs]
            self.answer = {
                'row': row,
                'column': column,
                'values': choices
            }
        except ValueError:
            self.raise_error()
