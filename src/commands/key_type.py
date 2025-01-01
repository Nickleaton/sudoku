"""KeyType module."""

from typing import Type


class KeyType:
    """Represents a key with an associated input_data type.

    Attributes:
        key (str): The name or identifier for the key.
        type (Type): The expected input_data type associated with the key.
    """

    def __init__(self, key: str, typ: Type):
        """Initialize a KeyType instance.

        Args:
            key (str): The name or identifier for the key.
            typ (Type): The expected input_data type associated with the key.
        """
        self.key: str = key
        self.type: Type = typ

    def __repr__(self):
        """Generate a string representation of the KeyType instance.

        Returns:
            str: A string in the format "KeyType(key='key', type='type')".
        """
        return f'KeyType(key={self.key!r}, type={self.type!r})'
