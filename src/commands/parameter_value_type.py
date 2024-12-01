"""ParameterValueType."""
from typing import Any, Type


class ParameterValueType:
    """Represents a parameter with a key, value, and associated type.

    Attributes:
        key (str): The identifier for the parameter.
        value (Any): The value associated with the parameter.
        type (Type): The expected data type for the value.
    """

    def __init__(self, key: str, value: Any, typ: Type):
        """Initialize a ParameterValueType instance.

        Args:
            key (str): The name or identifier for the parameter.
            value (Any): The value associated with the parameter.
            typ (Type): The expected data type for the parameter.

        Raises:
            TypeError: Raised if the value does not match the specified type,
                unless the type is `Any`.
        """
        self.key: str = key
        self.value: Any = value
        self.type: Type = typ
        if typ is not Any and not isinstance(value, typ):
            raise TypeError(f"Parameter {key} must be of type {typ}")

    def __repr__(self):
        """Returns a string representation of the ParameterValueType instance."""
        return f"ParameterValueType(key={self.key!r}, value={self.value!r}, type={self.type!r})"
