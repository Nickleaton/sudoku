"""CellPairEqualValueParser."""
from src.parsers.parser import Parser, ParserError
from src.tokens.cell_token import CellToken
from src.tokens.symbols import DashToken, EqualsToken
from src.tokens.value_token import ValueToken


class CellPairEqualValueParser(Parser):
    """Parser for cell pair equal value format, such as 'r1c1-r2c2=dd'."""

    def __init__(self):
        """Initialize the parser with a regular expression pattern for cell pair equal value format.

        The pattern matches a format like 'r1c1-r2c2=dd', where 'r1c1' and 'r2c2' are cell references
        and 'dd' is a value.
        """
        super().__init__(pattern=f"^{Parser.CELL}-{Parser.CELL}={Parser.VALUE}$", example_format="r1c1-r2c2=dd")
        self.token = CellToken() + DashToken() + CellToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> None:
        """Parse the input text for the cell pair equal value format.

        This method validates the input text against the defined regular expression pattern. If the
        text does not match the expected format, it raises a `ParserError`. It then splits the input
        into its constituent parts, extracting the rows, columns, and value.

        Args:
            text (str): The input string to be parsed, expected in the format 'r1c1-r2c2=dd'.

        Raises:
            ParserError: If the input text does not match the expected format.
            ValueError: If there is an issue parsing the values.
        """
        # Check if the input text matches the defined regular expression pattern.
        text = text.replace(" ", "")
        if not self.regular_expression.match(text):
            raise ParserError(
                f"{self.__class__.__name__} expects a cell pair equal value format like {self.example_format}")
        try:
            stripped_text: str = text.strip()
            lhs: str = stripped_text.split('=')[0]
            rhs: str = stripped_text.split('=')[1]
            cell1_str: str = lhs.split('-')[0]
            cell2_str: str = lhs.split('-')[1]
            r1: str = cell1_str[0]
            c1: str = cell1_str[1]
            r2: str = cell2_str[0]
            c2: str = cell2_str[1]
            self.result = [int(r1), int(c1), int(r2), int(c2), int(rhs)]
            self.answer = {
                "row1": r1,
                "column1": c1,
                "row2": r2,
                "column2": c2,
                "value": rhs
            }
        except ValueError:
            self.raise_error()
