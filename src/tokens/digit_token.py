"""DigitToken."""

from typing import ClassVar

from src.tokens.simple_token import SimpleToken


class DigitToken(SimpleToken):
    """Represents start single digit token (0-9)."""

    mapper: ClassVar[list[tuple[str, type]]] = [
        ('digit', int),
    ]

    def __init__(self) -> None:
        """Initialize start digit token with pattern 'd'."""
        super().__init__(pattern=r'(?P<digit>\d)')

    @property
    def description(self) -> str:
        """Get the description of the DigitToken.

        Returns:
            str: A description of the DigitToken's purpose and behavior.
        """
        return (
            'A digit token. Matches a single digit. Currently just 0-9, but it will be checked against the board.'
            'Going for a more generic digit token, for example for 16x16 boards will allow 0-9 and A-F.'
        )

    @property
    def example(self) -> str:
        """Get an example of a integer_value matched by the DigitToken.

        Returns:
            str: An example string that the DigitToken would match.
        """
        return '8'
