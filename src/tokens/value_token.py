from src.tokens.simple_token import SimpleToken


class ValueToken(SimpleToken):
    """Represents a token for matching Value"""

    def __init__(self):
        """Initializes a value token with pattern '(\d+)'."""
        super().__init__(r"(\d+)")


