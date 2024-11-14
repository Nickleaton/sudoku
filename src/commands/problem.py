"""Problem."""
from pydotted import pydot


class Problem(pydot):
    """A container for the components of a problem.

    This class represents a problem in a structured way, enabling easy
    access and management of various components related to the problem.
    It inherits from the `pydotted` library to provide dot notation access
    to attributes.
    """

    def __init__(self):
        """Initialize a new Problem instance.

        This constructor initializes the problem by calling the constructor
        of the parent class `pydot`. This allows the problem to hold components
        and provide dot notation access to them.

        Returns:
            None
        """
        super().__init__()
