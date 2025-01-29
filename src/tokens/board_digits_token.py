"""BoardDigitsToken."""
from src.tokens.simple_token import SimpleToken


class BoardDigitsToken(SimpleToken):
    """Represents allowed digits on a board."""

    def __init__(self) -> None:
        """Initialize digits token with start pattern."""
        super().__init__(pattern=r'(\d)\.\.(\d\d{0,1})')

    @property
    def description(self) -> str:
        """Get the description of the BoardDigitsToken.

        Returns:
            str: A description of the BoardDigitsToken's purpose and behavior.
        """
        return (
            'Digits on a board'
            'First allowed digit and .. then the last allowed digit.'
            'e.g  1..9'
            'or 1..15 for the case where the board is 16x16'
        )

    @property
    def example(self) -> str:
        """Get an example of a integer_value matched by the BoardDigitsToken.

        Returns:
            str: An example string that the BoardDigitsToken would match.
        """
        return '1..9'

    @property
    def is_abstract(self) -> bool:
        """Check if the token is abstract.

        This method returns `True` to indicate that the token is abstract.

        Returns:
            bool: `True` if the token is abstract, otherwise `False`.
        """
        return False
