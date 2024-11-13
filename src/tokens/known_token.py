"""KnownToken."""
from src.tokens.simple_token import SimpleToken


class KnownToken(SimpleToken):
    """Represents a token for matching a known value (0-9, l, m, h, e, o, f)."""

    def __init__(self):
        """Initialize a known token with pattern '([0-9.lmheof])'."""
        super().__init__(r"([0-9.lmheof])")
