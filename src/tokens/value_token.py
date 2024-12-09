"""ValueToken."""
from src.tokens.simple_token import SimpleToken


class ValueToken(SimpleToken):
    """Represent start token for matching Value."""

    def __init__(self):
        """Initialize start number token with pattern."""
        super().__init__(r'(\d+)')
