"""TestVariableType."""

import unittest
from math import log10

from src.utils.variable_type import VariableType


class TestVariableType(unittest.TestCase):
    """Test the VariableType class."""

    def test_format(self):
        """Test formatting of different VariableTypes."""
        self.assertEqual(VariableType.integer_number.format(1), "    1")  # Test integer format
        self.assertEqual(VariableType.log_integer.format(log10(9)), "    9")  # Test log_integer format
        self.assertEqual(VariableType.float_number.format(5.6), "5.600")  # Test float format
        self.assertEqual(VariableType.log_float.format(log10(2.5)), "2.500")  # Test log_float format
        self.assertEqual(VariableType.integer_number.format(None), ' None')  # Test integer format with None

    def test_repr(self):
        """Test the string representation of VariableTypes."""
        self.assertEqual("VariableType.integer_number", repr(VariableType.integer_number))  # Check repr for integer
        self.assertEqual("VariableType.log_integer", repr(VariableType.log_integer))  # Check repr for log_integer
        self.assertEqual("VariableType.float_number", repr(VariableType.float_number))  # Check repr for float
        self.assertEqual("VariableType.log_float", repr(VariableType.log_float))  # Check repr for log_float


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
