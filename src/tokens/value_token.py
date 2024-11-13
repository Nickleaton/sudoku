"""ValueToken."""
from src.tokens.simple_token import SimpleToken


class ValueToken(SimpleToken):
    """Represent a token for matching Value."""

    def __init__(self):
        """Initialize a value token with pattern."""
        super().__init__(r"(\d+)")
