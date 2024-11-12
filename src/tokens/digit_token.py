"""DigitToken."""
from src.tokens.simple_token import SimpleToken


class DigitToken(SimpleToken):
    """Represents a single digit token (0-9)."""

    def __init__(self):
        """Initialize a digit token with pattern 'd'."""
        super().__init__(r"\d")
