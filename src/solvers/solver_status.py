"""SolverStatus."""
from enum import Enum


class SolverStatus(Enum):
    """Enum representing the status of the solution."""

    not_solved = 'Not Solved'
    optimal = 'Optimal'
    infeasible = 'Infeasible'
    unbounded = 'Unbounded'
    undefined = 'Undefined'

    @classmethod
    def create(cls, status: str) -> 'SolverStatus':
        """Create a Status instance from a status string.

        Args:
            status (str): The status string to convert.

        Returns:
            SolverStatus: The corresponding Status instance.

        Raises:
            KeyError: If the provided status string does not match any Status.
        """
        try:
            return cls.__members__[status.lower()]
        except KeyError:
            choices: str = ', '.join(SolverStatus.__members__.keys())
            raise KeyError(f"Invalid status: '{status}'. Expected one of: {choices}")
