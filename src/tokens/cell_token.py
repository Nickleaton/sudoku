"""CellToken."""

from typing import ClassVar

from src.tokens.simple_token import SimpleToken


class CellToken(SimpleToken):
    """Represents start cell token with two digits."""

    mapper: ClassVar[list[tuple[str, type]]] = [
        ('row', int),
        ('col', int),
    ]

    def __init__(self) -> None:
        """Initialize start cell token with pattern 'dd' where the digits are row column."""
        super().__init__(pattern=r'(?P<row>\d)(?P<col>\d)')

    @property
    def description(self) -> str:
        """Get the description of the CellToken.

        Returns:
            str: A description of the CellToken's purpose and behavior.
        """
        return 'A cell reference. Two digits that are row and column.'

    @property
    def example(self) -> str:
        """Get an example of a integer_value matched by the CellToken.

        Returns:
            str: An example string that the CellToken would match.
        """
        return '12'
