from typing import List, Optional, Dict, Any

from src.parsers.parser import Parser, ParserError


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
        super().__init__(r"^\s*[TLBR]\s*\d\s*=\s*\d+\s*$")
        self.answer: Optional[Dict[str, Any]] = None

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
            text = text.replace(" ", "")
            side: str = text[0]  # Extracts side indicator (T, L, B, R)
            index: int = int(text[1])  # Converts the index portion to an integer
            value: int = int(text.split("=")[1])  # Extracts the value after '=' as integer

            # Save parsed components as a list.
            self.result = [side, index, value]
            self.answer = {
                "side": side,
                "index": index,
                "value": value
            }
        except ValueError:
            self.result = None
            raise ParserError(f"{self.__class__.__name__} expects valid input in the format 'T1=2' or similar")
