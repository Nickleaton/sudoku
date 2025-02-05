"""RegexUtils."""

import re


class RegexUtils:
    """RegexUtils."""

    # pylint: disable=too-few-public-methods

    @staticmethod
    def strip_names(pattern: str) -> str:
        """Remove all named groups from the given regex pattern.

        Args:
            pattern (str): The regex pattern to remove named groups from.

        Returns:
            str: The regex pattern with named groups removed.
        """
        return re.sub(r'\(\?P<[^>]+>', '(', pattern)
