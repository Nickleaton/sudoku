"""Enum for the type of variable."""
from enum import Enum


class VariableType(Enum):
    """Enumeration for variable types used in formatting value_list."""

    INT = 'int'
    FLOAT = 'float'
    LOG_INTEGER = 'log_int'
    LOG_FLOAT = 'log_float'

    def format(self, number: float | None) -> str:
        """Format start given input_value based on the variable type.

        Args:
            number (float | None): The input_value to format. If None, returns " None".

        Returns:
            str: The formatted string representation of the input_value based on its type.
        """
        if number is None:
            return ' None'

        format_map = {
            VariableType.INT: lambda formatted_number: f'{number:5.0f}',
            VariableType.FLOAT: lambda formatted_number: f'{number:5.3f}',
            VariableType.LOG_INTEGER: lambda formatted_number: f'{pow(10, number):5.0f}',
            VariableType.LOG_FLOAT: lambda formatted_number: f'{pow(10, number):5.3f}',
        }
        formatter = format_map.get(self)
        if formatter:
            return formatter(number)

        return 'Unknown'  # pragma: no cover

    def __repr__(self) -> str:
        """Return the string representation of the VariableType.

        Returns:
            str: The representation of the VariableType.
        """
        return f'VariableType.{self.name}'
