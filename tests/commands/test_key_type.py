import unittest
from typing import Any

from src.commands.key_type import KeyType


class TestKeyType(unittest.TestCase):
    """Unit tests for the KeyType class."""

    def setUp(self) -> None:
        """Set up test cases."""
        self.valid_key = "example_key"
        self.valid_type = int

    def test_initialization_valid(self):
        """Test initializing with a valid key and type."""
        key_type = KeyType(self.valid_key, self.valid_type)
        self.assertEqual(key_type.key, self.valid_key)
        self.assertEqual(key_type.type, self.valid_type)

    def test_initialization_with_custom_type(self):
        """Test initializing with a custom type."""

        class CustomType:
            pass

        key_type = KeyType("custom_key", CustomType)
        self.assertEqual(key_type.key, "custom_key")
        self.assertEqual(key_type.type, CustomType)

    def test_initialization_with_any_type(self):
        """Test initializing with the Any type."""
        key_type = KeyType(self.valid_key, Any)
        self.assertEqual(key_type.key, self.valid_key)
        self.assertEqual(key_type.type, Any)

    def test_initialization_empty_key(self):
        """Test initializing with an empty string as a key."""
        key_type = KeyType("", self.valid_type)
        self.assertEqual(key_type.key, "")
        self.assertEqual(key_type.type, self.valid_type)

    def test_initialization_edge_cases(self):
        """Test initializing with edge cases for the key."""
        special_key = "!@#$%^&*()"
        key_type = KeyType(special_key, str)
        self.assertEqual(key_type.key, special_key)
        self.assertEqual(key_type.type, str)

    def test_repr(self):
        """Test the string representation (__repr__) of the KeyType instance."""
        key_type = KeyType(self.valid_key, self.valid_type)
        repr_str = repr(key_type)
        expected_repr = f"KeyType(key={self.valid_key!r}, type={self.valid_type!r})"
        self.assertEqual(repr_str, expected_repr)


if __name__ == "__main__":
    unittest.main()
