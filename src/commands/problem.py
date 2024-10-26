from pydotted import pydot


class Problem(pydot):
    """
    Payload for a problem.

    This class represents a problem in a structured way, allowing
    for configuration and management of various problem components.
    It inherits from the `pydotted` library for dot notation access to attributes.
    """

    def __init__(self):
        """
        Initialize a new Problem instance.

        This constructor initializes the problem payload by calling the
        constructor of the parent class `pydot`.
        """
        super().__init__()
