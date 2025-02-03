"""CellToken."""
from typing import Type

from src.tokens.simple_token import SimpleToken


class BoxToken(SimpleToken):
    """Represents the box size."""

    mapper: list[tuple[str, Type]] = [
        ('rows', int),
        ('cols', int),
    ]

    def __init__(self) -> None:
        """Initialize start cell token with pattern 'dxd' where its row x column."""
        super().__init__(pattern=r'(?P<rows>\d)x(?P<cols>\d)')

    @property
    def description(self) -> str:
        """Get the description of the CellToken.

        Returns:
            str: A description of the CellToken's purpose and behavior.
        """
        return 'A box size dxd where its rxc for rows by columns.'

    @property
    def example(self) -> str:
        """Get an example of digit matched by the BoxToken.

        Returns:
            str: An example string that the BoxToken would match.
        """
        return '9x9'

