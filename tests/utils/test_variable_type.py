"""TestVariableType."""

import unittest
from math import log10
from src.utils.variable_type import VariableType


class TestVariableType(unittest.TestCase):
    """Test the VariableType class."""

    def test_format(self):
        """Test formatting of different VariableTypes."""
        self.assertEqual(VariableType.INT.format(1), "    1")  # Test INT format
        self.assertEqual(VariableType.LOG_INTEGER.format(log10(9)), "    9")  # Test LOG_INTEGER format
        self.assertEqual(VariableType.FLOAT.format(5.6), "5.600")  # Test FLOAT format
        self.assertEqual(VariableType.LOG_FLOAT.format(log10(2.5)), "2.500")  # Test LOG_FLOAT format
        self.assertEqual(VariableType.INT.format(None), ' None')  # Test INT format with None

    def test_repr(self):
        """Test the string representation of VariableTypes."""
        self.assertEqual("VariableType.INT", repr(VariableType.INT))  # Check repr for INT
        self.assertEqual("VariableType.LOG_INTEGER", repr(VariableType.LOG_INTEGER))  # Check repr for LOG_INTEGER
        self.assertEqual("VariableType.FLOAT", repr(VariableType.FLOAT))  # Check repr for FLOAT
        self.assertEqual("VariableType.LOG_FLOAT", repr(VariableType.LOG_FLOAT))  # Check repr for LOG_FLOAT


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
