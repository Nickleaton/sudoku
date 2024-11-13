"""SideToken."""
from src.tokens.simple_token import SimpleToken


class SideToken(SimpleToken):
    """Represents a token for matching a side indicator (T, L, B, R)."""

    def __init__(self):
        """Initialize a side token with pattern '([TLBR])'."""
        super().__init__(r"([TLBR])")
