"""TestCyclic."""
import unittest

from src.utils.cyclic import Cyclic


class TestSide(unittest.TestCase):
    """Test the Cyclic class."""

    def test_create(self):
        """Test creating Cyclic instances from string inputs."""
        self.assertEqual(Cyclic.ANTICLOCKWISE, Cyclic.create("A"))
        self.assertEqual(Cyclic.CLOCKWISE, Cyclic.create("C"))
        with self.assertRaises(ValueError):
            Cyclic.create('X')

    def test_repr(self):
        """Test the string representation of Cyclic instances."""
        self.assertEqual('Cyclic.CLOCKWISE', repr(Cyclic.CLOCKWISE))
        self.assertEqual('Cyclic.ANTICLOCKWISE', repr(Cyclic.ANTICLOCKWISE))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
