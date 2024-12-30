"""Enum for the type of value_variable."""
from enum import Enum
from typing import Callable


class VariableType(Enum):
    """Enumeration for value_variable types used in formatting value_list."""

    integer_number = 'integer'
    float_number = 'float'
    log_integer = 'log_int'
    log_float = 'log_float'

    def format(self, number: float | None) -> str:
        """Format start given input_value based on the value_variable type.

        Args:
            number (float | None): The input_value to format. If None, returns " None".

        Returns:
            str: The formatted string representation of the input_value based on its type.
        """
        if number is None:
            return ' None'

        format_map: dict['VariableType', Callable[[float], str]] = {
            VariableType.integer_number: lambda formatted_number: f'{number:5.0f}',
            VariableType.float_number: lambda formatted_number: f'{number:5.3f}',
            VariableType.log_integer: lambda formatted_number: f'{pow(10, number):5.0f}',
            VariableType.log_float: lambda formatted_number: f'{pow(10, number):5.3f}',
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
