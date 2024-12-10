"""ParameterValueType."""
from typing import Any, Type


class ParameterValueType:
    """Represent a start parameter with a key, associated input_value, and expected type.

    Attributes:
        key (str): The identifier for the parameter.
        parameter_value (Any): The input_value associated with the parameter.
        typ (Type): The expected data type for the input_value.
    """

    def __init__(self, key: str, parameter_value: Any, typ: Type):
        """Initialize a ParameterValueType instance.

        Args:
            key (str): The name or identifier for the parameter.
            parameter_value (Any): The input_value associated with the parameter.
            typ (Type): The expected data type for the parameter.

        Raises:
            TypeError: If the input_value does not match the specified type, unless the type is `Any`.
        """
        self.key: str = key
        self.parameter_value: Any = parameter_value
        self.type: Type = typ
        if typ is not Any and not isinstance(parameter_value, typ):
            raise TypeError(f'Parameter {key} must be of type {typ}')

    def __repr__(self):
        """Return the string representation of the ParameterValueType instance.

        Returns:
            str: A string representing the ParameterValueType instance.
        """
        return f'ParameterValueType(key={self.key!r}, number={self.parameter_value!r}, type={self.type!r})'
