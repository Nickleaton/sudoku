"""TestMinMax."""
import unittest

from src.utils.minmax import MinMax


class TestMinMax(unittest.TestCase):
    """Test the MinMax class constants."""

    def test_repr(self):
        """Check the string representation of MinMax constants."""
        self.assertEqual('MinMax.minimum', repr(MinMax.minimum))
        self.assertEqual('MinMax.maximum', repr(MinMax.maximum))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
