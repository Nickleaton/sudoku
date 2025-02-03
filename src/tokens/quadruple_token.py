"""QuadrupleToken."""
from typing import Type

from src.tokens.simple_token import SimpleToken


class QuadrupleToken(SimpleToken):
    """Represents start token for matching one or more digits or question marks."""

    mapper: list[tuple[str, Type]] = [
        ('quads', list),
    ]

    def __init__(self) -> None:
        """Initialize start quad token with start pattern of digits."""
        super().__init__(pattern=r'(?P<quads>[\d]{0,4})')

    @property
    def description(self) -> str:
        """Get the description of the QuadrupleToken.

        Returns:
            str: A description of the QuadrupleToken's purpose and behavior.
        """
        return (
            'A quadruple token. Matches one or more digits. '
            'Those digits must appear in the surrounding cells. '
        )

    @property
    def example(self) -> str:
        """Get an example of a integer_value matched by the QuadrupleToken.

        Returns:
            str: An example string that the QuadrupleToken would match.
        """
        return '123'
