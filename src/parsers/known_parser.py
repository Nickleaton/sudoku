"""KnownParser."""
import re

from src.parsers.parser import Parser
from src.tokens.known_token import KnownToken
from src.tokens.token import OneOrMoreToken, Token
from src.utils.sudoku_exception import SudokuError


class KnownParser(Parser):
    """Parse start known string containing known value_list or restricted conditions."""

    token: Token = OneOrMoreToken(KnownToken())

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
        )

    def parse(self, text: str) -> dict:
        """Parse the input string and store the parsed_data in the 'parsed_data' attribute.

        Args:
            text (str): The input text to be parsed

        Returns:
            dict: A dictionary containing the parsed data.

        Raises:
            SudokuError: If the input text cannot be parsed.
        """
        match = re.fullmatch(self.token.pattern, text)
        if match is None:
            raise SudokuError(f'Could not parse {text!r}')
        return {'Known': [KnownToken().parse(part)['cell'] for part in list(text)]}
