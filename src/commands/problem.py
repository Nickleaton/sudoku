"""Problem."""
from pydotted import pydot


class Problem(pydot):
    """A container for the components of a problem.

    This class represents a problem in a dynamic way.
    It inherits from the `pydotted` library to provide dot notation access
    to attributes.
    """

    def __str__(self) -> str:
        """Return a string of the keys."""
        return f"| {', '.join(self.keys())} |"
