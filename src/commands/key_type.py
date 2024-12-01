"""KeyType."""

from typing import Type


class KeyType:
    """Represents a key with an associated data type.

    Attributes:
        key (str): The name or identifier for the key.
        type (Type): The expected data type for the value associated with the key.
    """

    def __init__(self, key: str, typ: Type):
        """Initializes a KeyType instance.

        Args:
            key (str): The name or identifier for the key.
            typ (Type): The expected data type for the value associated with the key.
        """
        self.key: str = key
        self.type: Type = typ

    def __repr__(self):
        """Returns a string representation of the KeyType instance."""
        return f"KeyType(key={self.key!r}, type={self.type!r})"

