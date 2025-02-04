"""Tags."""
from typing import Any

from pydotted import pydot


class Tags(pydot):
    """Represents a collection of tags that can be compared and converted to a dictionary."""

    def __eq__(self, other: object) -> bool:
        """Check equality between two Tags objects.

        Args:
            other (object): The object to compare with the current instance.

        Returns:
            bool: True if the other object is a Tags instance and has the same dictionary representation,
                  False otherwise.
        """
        if not isinstance(other, Tags):
            return NotImplemented
        return self.to_dict() == other.to_dict()

    def to_dict(self) -> dict[str, Any]:
        """Convert the Tags object back to a dictionary for comparison.

        Returns:
            dict[str, Any]: A dictionary representation of the Tags object,
                             where the keys are the tag names and the values are their corresponding values.
        """
        return {key: self[key] for key in self.keys()}

    def __repr__(self) -> str:
        """Return a string representation of the Tags object.

        Returns:
            str: A string representation of the Tags object.
        """
        return f'{self.__class__.__name__}({self.to_dict()})'
