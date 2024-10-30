from typing import Dict, Optional

from src.parsers.parser import Parser, ParserError


class LittleKillersParser(Parser):
    """Parser for the Little Killers format."""

    def __init__(self):
        """Initializes the LittleKillersParser with a regex pattern for valid input formats."""
        super().__init__(r"^\s*[TLBR]\s*\d\s*[C|A]\s*=\s*\d+\s*$")
        self.answer: Optional[Dict[str, int]] = None

    def parse(self, text: str) -> None:
        """Parses the input text to extract components of the Little Killers format.

        Args:
            text (str): The input text expected to be in the format 'T1C=2' or similar.

            First letter is T, L, B, or R corresponding to the side of the board, Top, Left, Right or Bottom.
            Second number is the index of the cell. Column or row index
            Third letter is C or A corresponding to the direction of the cell, Clockwise or Anticlockwise.
            Last number is the value depending on the constraint

        Raises:
            ParserError: If the input text does not match the expected format
                          or if conversion to integers fails.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects input in the format 'T1C=2' or similar")

        try:
            # Remove whitespace from the input text.
            text = text.replace(" ", "")

            # Extract the components based on the specified format.
            side: str = text[0]  # The first character (T, L, B, R)
            index: int = int(text[1])  # The second character as an integer index
            direction: str = text[2]  # The third character (C or A)
            value: int = int(text.split("=")[1])  # The value after '='

            # Store the extracted components in the result attribute.
            self.result = [side, index, direction, value]
            self.answer = {
                'side': side,
                'index': index,
                'direction': direction,
                'value': value
            }
        except ValueError:
            # If any of the values cannot be converted or extracted, clear the result and raise an error.
            self.result = None
            raise ParserError(f"{self.__class__.__name__} expects valid input in the format 'T1C=2' or similar")
