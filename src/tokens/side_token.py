"""SideToken."""
from src.tokens.simple_token import SimpleToken


class SideToken(SimpleToken):
    """Represents start token for matching start side indicator (T, L, B, R)."""

    def __init__(self):
        """Initialize start side token with pattern '([TLBR])'."""
        super().__init__('([TLBR])')
