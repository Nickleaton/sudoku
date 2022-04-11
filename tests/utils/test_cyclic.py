import unittest

from src.utils.cyclic import Cyclic


class TestSide(unittest.TestCase):

    def test_create(self):
        self.assertEqual(Cyclic.ANTICLOCKWISE, Cyclic.create("A"))
        self.assertEqual(Cyclic.CLOCKWISE, Cyclic.create("C"))
        with self.assertRaises(ValueError):
            Cyclic.create('X')

    def test_repr(self):
        self.assertEqual('Cyclic.CLOCKWISE', repr(Cyclic.CLOCKWISE))
        self.assertEqual('Cyclic.ANTICLOCKWISE', repr(Cyclic.ANTICLOCKWISE))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
