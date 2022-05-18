import unittest

from src.utils.minmax import MinMax


class TestMinMax(unittest.TestCase):

    def test_repr(self):
        self.assertEqual('MinMax.MINIMUM', repr(MinMax.MINIMUM))
        self.assertEqual('MinMax.MAXIMUM', repr(MinMax.MAXIMUM))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
