"""Enum for the type of variable."""
from enum import Enum
from typing import Optional


class VariableType(Enum):
    """Enumeration for variable types used in formatting values."""

    INT = 'int'
    FLOAT = 'float'
    LOG_INTEGER = 'log_int'
    LOG_FLOAT = 'log_float'

    def format(self, value: Optional[float]) -> str:
        """Format a given value based on the variable type.

        Args:
            value (Optional[float]): The value to format. If None, returns " None".

        Returns:
            str: The formatted string representation of the value based on its type.
        """
        if value is None:
            return " None"
        if self == VariableType.INT:
            return f"{value:5.0f}"
        if self == VariableType.FLOAT:
            return f"{value:5.3f}"
        if self == VariableType.LOG_INTEGER:
            return f"{pow(10, value):5.0f}"
        if self == VariableType.LOG_FLOAT:
            return f"{pow(10, value):5.3f}"
        return "Unknown"  # pragma: no cover

    def __repr__(self) -> str:
        """Return the string representation of the VariableType.

        Returns:
            str: The representation of the VariableType.
        """
        return f"VariableType.{self.name}"
