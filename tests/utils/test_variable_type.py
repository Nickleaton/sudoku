import unittest
from math import log10

from src.utils.variable_type import VariableType


class TestVariableType(unittest.TestCase):

    def test_format(self):
        self.assertEqual(VariableType.INT.format(1), "    1")
        self.assertEqual(VariableType.LOG_INTEGER.format(log10(9)), "    9")
        self.assertEqual(VariableType.FLOAT.format(5.6), "5.600")
        self.assertEqual(VariableType.LOG_FLOAT.format(log10(2.5)), "2.500")


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
