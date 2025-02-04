"""LittleKillerParser."""
import re

from src.parsers.parser import Parser
from src.tokens.cycle_token import CycleToken
from src.tokens.digit_token import DigitToken
from src.tokens.side_token import SideToken
from src.tokens.symbols import EqualsToken
from src.tokens.token import Token
from src.tokens.value_token import ValueToken
from src.utils.sudoku_exception import SudokuError


class LittleKillerParser(Parser):
    """Parser for the Little Killers format."""

    token: Token = SideToken() + DigitToken() + CycleToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> dict:
        """Parse the input text to extract components of the Little Killers format.

        Args:
            text (str): The input text to be parsed

        Returns:
            dict: A dictionary containing the parsed data.
        """
        match = re.fullmatch(self.token.pattern, text)
        if match is None:
            raise SudokuError(f'Could not parse {text!r}')

        side_text: str = text[0]
        index_text: str = text[1]
        cycle_text: str = text[2]
        target_text: str = text.split('=')[1]

        # Store the extracted components in the parsed_data attribute.
        return {
            'LittleKiller': {
                'Side': SideToken().parse(side_text)['side'],
                'Index': DigitToken().parse(index_text)['digit'],
                'Cyclic': CycleToken().parse(cycle_text)['cycle'],
                'Value': ValueToken().parse(target_text)['value'],
            }
        }
