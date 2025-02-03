"""OrderToken."""
from typing import Type

from src.tokens.simple_token import SimpleToken


class OrderToken(SimpleToken):
    """Represents a token for matching a order indicator (I, D, U)."""

    mapper: list[tuple[str, Type]] = [
        ('order', str),
    ]

    def __init__(self) -> None:
        """Initialize token with pattern '([IDU])' for clockwise and anticlockwise."""
        super().__init__(pattern=r'(?P<order>[IDU])')

    @property
    def description(self) -> str:
        """Get the description of the OrderToken.

        Returns:
            str: A description of the OrderToken's purpose and behavior.
        """
        return 'An increasing, decreasing, or unordered indicator. I D or U'

    @property
    def example(self) -> str:
        """Get an example of a value  matched by the OrderToken.

        Returns:
            str: An example string that the OrderToken would match.
        """
        return 'I'
