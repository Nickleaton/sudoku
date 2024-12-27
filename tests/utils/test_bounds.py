"""TestBounds."""
import unittest

from src.utils.bounds import Bounds


class TestBounds(unittest.TestCase):
    """Test the Bounds class."""

    def test_repr(self):
        """Test the __repr__ method for Bounds enum value_list."""
        self.assertEqual('Bounds.lower', repr(Bounds.lower))
        self.assertEqual('Bounds.upper', repr(Bounds.upper))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
