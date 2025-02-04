"""BoardDigitsParser."""

from src.parsers.parser import Parser
from src.tokens.board_digits_token import BoardDigitsToken
from src.tokens.token import Token


class BoardDigitsParser(Parser):
    """Parser for BoardDigits Sizes."""

    token: Token = BoardDigitsToken()

    def parse(self, text: str) -> dict:
        """Parse the input text to extract rows and column.

        Args:
            text (str): The input text to be parsed

        Returns:
            dict: A dictionary containing the parsed data.
        """
        return BoardDigitsParser().parse(text)
