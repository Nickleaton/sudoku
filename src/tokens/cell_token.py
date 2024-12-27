"""CellToken."""
from src.tokens.simple_token import SimpleToken


class CellToken(SimpleToken):
    """Represents start cell token with two digits."""

    def __init__(self) -> None:
        """Initialize start cell token with pattern 'dd' where the digits are row column."""
        super().__init__(pattern=r'(\d)(\d)')

    @property
    def description(self) -> str:
        """Get the description of the CellToken.

        Returns:
            str: A description of the CellToken's purpose and behavior.
        """
        return 'A cell reference. Two digits that are row and column.'

    @property
    def example(self) -> str:
        """Get an example of a value matched by the CellToken.

        Returns:
            str: An example string that the CellToken would match.
        """
        return '12'

    @property
    def is_abstract(self) -> bool:
        """Check if the token is abstract.

        This method returns `True` to indicate that the token is abstract.

        Returns:
            bool: `True` if the token is abstract, otherwise `False`.
        """
        return False
