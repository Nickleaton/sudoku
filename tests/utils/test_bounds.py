"""TestBounds."""
import unittest

from src.utils.bounds import Bounds


class TestBounds(unittest.TestCase):
    """Test the Bounds class."""

    def test_repr(self):
        """Test the __repr__ method for Bounds enum values."""
        self.assertEqual('Bounds.LOWER', repr(Bounds.LOWER))
        self.assertEqual('Bounds.UPPER', repr(Bounds.UPPER))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
