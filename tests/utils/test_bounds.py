import unittest

from src.utils.bounds import Bounds


class TestBounds(unittest.TestCase):

    def test_repr(self):
        self.assertEqual('Bounds.LOWER', repr(Bounds.LOWER))
        self.assertEqual('Bounds.UPPER', repr(Bounds.UPPER))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
