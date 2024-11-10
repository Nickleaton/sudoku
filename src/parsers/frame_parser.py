from typing import List, Optional

from src.parsers.parser import Parser, ParserError
from src.tokens.digit_token import DigitToken
from src.tokens.side_token import SideToken
from src.tokens.symbols import EqualsToken
from src.tokens.value_token import ValueToken


class FrameParser(Parser):
    """Parser for extracting side, index, and value from a string format like 'T1=2'.

    This parser matches a specified string pattern, removes whitespace,
    and extracts components including a side indicator (T, L, B, R),
    an integer index, and a value after '='.
    """

    result: Optional[List[int]] = None

    def __init__(self):
        """Initializes FrameParser with a regex pattern.

        The regex pattern expects a string format of 'T1=2' with optional
        whitespace, where the side is one of 'T', 'L', 'B', or 'R', followed
        by a numeric index and a value separated by '='.
        """
        super().__init__(pattern=r"^\s*[TLBR]\s*\d\s*=\s*\d+\s*$", example_format="[TLBR]i=v")
        self.token = SideToken() + DigitToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> None:
        """Parses the input string to extract side, index, and value.

        Args:
            text (str): The string input in the format 'T1=2' or similar.

        Raises:
            ParserError: If the input string does not match the expected pattern,
                         or if parsing fails due to invalid format.
        """
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects input in the format 'T1=2' or similar")

        try:
            # Remove spaces to standardize input format.
            stripped_text: str = text.replace(" ", "")
            lhs: str = stripped_text.split("=")[0]
            rhs: str = stripped_text.split("=")[1]
            side: str = lhs[0]  # Extracts side indicator (T, L, B, R)
            index: str = lhs[1]
            value: str = rhs

            # Save parsed components as a list.
            self.result = [side, int(index), int(value)]  # type: ignore[list-item]
            self.answer = {
                "side": side,
                "index": index,
                "value": value
            }
        except ValueError:
            self.raise_error()
