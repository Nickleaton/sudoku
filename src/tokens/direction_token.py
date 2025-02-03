"""DirectionToken."""
from src.tokens.simple_token import SimpleToken


class DirectionToken(SimpleToken):
    """Represents a token for matching a direction (UP_LEFT, UP, UP_RIGHT ...)."""

    def __init__(self) -> None:
        """Initialize token with pattern for directions."""
        # Regular expression to match valid direction tokens (UR, UL, DL, DR, U, D, L, R),
        # while excluding invalid combinations (UD, DU, LR, RL).
        #
        # The pattern is explained as follows:
        #
        # (?P<direction>...)  - Named capturing group 'direction' that captures the matched direction.
        #
        # (?!UD|DU|LR|RL)    - Negative lookahead to exclude invalid combinations: UD, DU, LR, RL.
        #                       This ensures that strings containing any of these pairs are not matched.
        #
        # Must come before the valid direction tokens, to ensure that they are not matched when the negative lookahead
        # condition is not satisfied.
        #
        # (UR|UL|DL|DR|U|D|L|R)  - Matches one of the valid direction tokens: UR, UL, DL, DR, U, D, L, R.
        #                          This part matches the valid directions after ensuring the negative
        #                          lookahead condition is satisfied.
        super().__init__(pattern='(?P<direction>(?!UD|DU|LR|RL)(UR|UL|DL|DR|U|D|L|R))')

    @property
    def description(self) -> str:
        """Get the description of the DirectionToken.

        Returns:
            str: Indicates the direction in a grid or coordinate system.
        """
        return 'A direction indicator. One of UL, U, UR, L, R, DL, D, DR.'

    @property
    def example(self) -> str:
        """Get an example of a integer_value matched by the CycleToken.

        Returns:
            str: An example string that the CycleToken would match.
        """
        return 'UL'
