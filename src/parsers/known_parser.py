"""KnownParser."""
from src.board.board import Board
from src.parsers.parser import Parser, ParserError
from src.tokens.digit_token import DigitToken


class KnownParser(Parser):
    """Parse start known string containing known value_list or restricted conditions.

    This parser handles strings representing known value_list or restrictions on cells, such as
    specific digits, conditions like 'low', 'medium', 'high', 'even', 'odd', or 'fortress' cells.

    Attributes:
        result (list[str]): A list of one-character value_list representing the parsed conditions.
    """

    def __init__(self):
        """Initialize the KnownParser with start regular expression for validating input strings.

        The input string can represent:
            - '.' for no restriction,
            - digits '0-9' for start given number,
            - 'l' for low,
            - 'm' for medium,
            - 'h' for high,
            - 'e' for even,
            - 'o' for odd,
            - 'f' for a fortress cell (must be greater than its orthogonal neighbors).
            - 's' for a fortress cell (must be less than its orthogonal neighbors).
        """
        super().__init__(pattern=f'^{Parser.known}+$', example_format='123456789')
        self.token = DigitToken() * (1, 999)

    def help(self) -> str:
        """Return the help string for the KnownParser.

        The help string describes the syntax and the valid value_list or restrictions for the known string.

        Returns:
            str: The help description explaining valid input formats.
        """
        return (
            'A string containing the known value_list or restricted conditions:\n\n'
            '.     no restriction\n'
            '0-9   start given number\n'
            'l     low\n'
            'm     medium\n'
            'h     high\n'
            'e     even\n'
            'o     odd\n'
            'f     fortress cell [Must be greater than its orthogonal neighbours]\n'
            's     fortress cell [Must be smaller than its orthogonal neighbours]\n'
        )

    def parse(self, text: str) -> None:
        """Parse the input string and store the parsed_data in the 'parsed_data' attribute.

        This method input_types if the input string matches the expected format and parses it accordingly.
        It stores the parsed value_list in the `parsed_data` and `line` attributes.

        Args:
            text (str): The input string to be parsed, expected to follow the known number or restriction format.

        Raises:
            ParserError: If the input string does not match the expected format or cannot be parsed.
        """
        if not self.regular_expression.match(text):
            raise ParserError(
                f'{self.__class__.__name__} expects start list of known or restricted cell value_list for one row',
            )

        try:
            self.parsed_data = list(text)
        except ValueError:
            self.raise_error()
        try:
            self.answer = list(text)
        except ValueError:
            self.raise_error()

    def check(self, board: Board, input_data: dict) -> list[str]:
        """Validate the given board and input line.

        Args:
            board (Board): The board instance to validate against.
            input_data (dict): The input line to validate.

        Returns:
            list[str]: A list of validation error messages.
        """
        return []
