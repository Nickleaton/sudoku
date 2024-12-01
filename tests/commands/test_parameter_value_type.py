import unittest
from typing import Any

from src.commands.parameter_value_type import ParameterValueType


class TestParameterValueType(unittest.TestCase):
    """Unit tests for the ParameterValueType class."""

    def setUp(self) -> None:
        """Set up test cases."""
        self.valid_key = "test_key"
        self.valid_value = 42
        self.valid_type = int

    def test_initialization_valid(self):
        """Test initializing with valid key, value, and type."""
        param = ParameterValueType(self.valid_key, self.valid_value, self.valid_type)
        self.assertEqual(param.key, self.valid_key)
        self.assertEqual(param.value, self.valid_value)
        self.assertEqual(param.type, self.valid_type)

    def test_initialization_type_mismatch(self):
        """Test initialization fails when value does not match type."""
        with self.assertRaises(TypeError) as context:
            ParameterValueType(self.valid_key, "not an int", self.valid_type)
        self.assertIn("Parameter test_key must be of type <class 'int'>", str(context.exception))

    def test_initialization_with_any_type(self):
        """Test initializing with the Any type (accepts any value)."""
        param = ParameterValueType(self.valid_key, "any value", Any)
        self.assertEqual(param.key, self.valid_key)
        self.assertEqual(param.value, "any value")
        self.assertEqual(param.type, Any)

    def test_initialization_with_custom_type(self):
        """Test initializing with a custom type."""

        class CustomType:
            pass

        custom_value = CustomType()
        param = ParameterValueType("custom_key", custom_value, CustomType)
        self.assertIsInstance(param.value, CustomType)
        self.assertEqual(param.type, CustomType)

    def test_type_check_on_edge_case(self):
        """Test initialization with a value on type edge cases."""
        param = ParameterValueType("key", 3.0, float)
        self.assertEqual(param.value, 3.0)
        self.assertEqual(param.type, float)

    def test_repr(self):
        """Test the string representation (__repr__) of the ParameterValueType instance."""
        param = ParameterValueType(self.valid_key, self.valid_value, self.valid_type)
        repr_str = repr(param)
        expected_repr = f"ParameterValueType(key={self.valid_key!r}, value={self.valid_value!r}, type={self.valid_type!r})"
        self.assertEqual(repr_str, expected_repr)


if __name__ == "__main__":
    unittest.main()