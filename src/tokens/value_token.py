"""ValueToken."""
from src.tokens.simple_token import SimpleToken


class ValueToken(SimpleToken):
    """Represents a token for matching values."""

    def __init__(self):
        """Initialize the token with a regex pattern for one or more digits."""
        super().__init__(r'(\d+)')

    @property
    def description(self) -> str:
        """Get the description of the ValueToken.

        Returns:
            str: A description of the ValueToken's purpose and behavior.
        """
        return 'A value token. Matches one or more digits. This token is used for identifying numeric values.'

    @property
    def example(self) -> str:
        """Get an example of a value matched by the ValueToken.

        Returns:
            str: An example string that the ValueToken would match.
        """
        return '42'

    @property
    def is_abstract(self) -> bool:
        return False
