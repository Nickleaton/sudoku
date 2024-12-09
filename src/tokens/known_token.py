"""KnownToken."""
from src.tokens.simple_token import SimpleToken


class KnownToken(SimpleToken):
    """Represents start token for matching start known number (0-9, l, m, h, e, o, f)."""

    def __init__(self):
        """Initialize start known token with pattern '([0-9.lmheof])'."""
        super().__init__('([0-9.lmheof])')
