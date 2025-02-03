"""ValueToken."""
from typing import Type

from src.tokens.simple_token import SimpleToken


class ValueToken(SimpleToken):
    """Represents a token for matching cell_values."""

    mapper: list[tuple[str, Type]] = [

        ('value', int),
    ]

    def __init__(self) -> None:
        """Initialize the token with a regex pattern for one or more digits."""
        super().__init__(r'(?P<value>\d+)')

    @property
    def description(self) -> str:
        """Get the description of the ValueToken.

        Returns:
            str: A description of the ValueToken's purpose and behavior.
        """
        return 'A integer_value token. Matches one or more digits. This token is used for numeric cell_values.'

    @property
    def example(self) -> str:
        """Get an example of a integer_value matched by the ValueToken.

        Returns:
            str: An example string that the ValueToken would match.
        """
        return '42'
