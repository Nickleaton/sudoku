"""TestCyclic."""
import unittest

from src.utils.cyclic import Cyclic


class TestSide(unittest.TestCase):
    """Test the Cyclic class."""

    def test_create(self):
        """Test creating Cyclic instances from string input_types."""
        self.assertEqual(Cyclic.anticlockwise, Cyclic.create("A"))
        self.assertEqual(Cyclic.clockwise, Cyclic.create("C"))
        with self.assertRaises(ValueError):
            Cyclic.create('X')

    def test_repr(self):
        """Test the string representation of Cyclic instances."""
        self.assertEqual('Cyclic.clockwise', repr(Cyclic.clockwise))
        self.assertEqual('Cyclic.anticlockwise', repr(Cyclic.anticlockwise))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
