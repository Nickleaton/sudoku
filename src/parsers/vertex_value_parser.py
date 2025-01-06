"""VertexValueParser."""

from src.board.board import Board
from src.parsers.parser import Parser, ParserError
from src.tokens.cell_token import CellToken
from src.tokens.symbols import EqualsToken
from src.tokens.value_token import ValueToken


class VertexValueParser(Parser):
    """Parser for Vertex Value format: 'dd=d' where dd are two digits and d is one or more digits."""

    def __init__(self):
        """Initialize the VertexValueParser with start regex pattern for the Vertex Value format."""
        super().__init__(pattern=r'^\d{2}=\d+$', example_format='rc=dd')
        self.token = CellToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> None:
        """Parse the input text to extract vertex number components.

        Args:
            text (str): The input text expected to be in the format 'dd=d'.

        Raises:
            ParserError: If the input text does not match the expected format.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f'{self.__class__.__name__} expects format like "dd=d"')

        # Split the text at the equals sign to extract components.
        parts: list[str] = text.split('=')
        lhs: str = parts[0]
        rhs: str = parts[1]

        # Store results in the parsed_data attribute.
        self.parsed_data = [int(lhs[0]), int(lhs[1]), int(rhs)]
        self.answer = {
            'row': lhs[0],
            'column': lhs[1],
            'number': rhs,
        }

    def check(self, board: Board, input_data: dict) -> list[str]:
        """Validate the provided input line against the given board.

        This function currently returns an empty list of errors, but it can be extended
        to validate the input line according to the board's constraints.

        Args:
            board (Board): The board object containing the validation rules or constraints.
            input_data (dict): A dictionary containing the line to validate.

        Returns:
            list[str]: A list of error messages. Empty if no errors are found.
        """
        return []
