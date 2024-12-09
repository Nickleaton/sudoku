"""Problem module."""

from pydotted import pydot


class Problem(pydot):
    """A container for the components of a problem.

    Represents a dynamic container for the components of a problem.
    Inherits from the `pydotted` library to enable dot notation access
    for its attributes.
    """

    def __str__(self) -> str:
        """Convert the problem's keys to a string representation.

        Returns:
            str: A string listing the keys.
        """
        return f"| {', '.join(self.keys())} |"
