import unittest

from src.utils.functions import Functions


class TestFunctions(unittest.TestCase):

    def test_triangular(self):
        self.assertEqual(1, Functions.triangular(1))
        self.assertEqual(3, Functions.triangular(2))
        self.assertEqual(6, Functions.triangular(3))
        self.assertEqual(10, Functions.triangular(4))
        self.assertEqual(15, Functions.triangular(5))
        self.assertEqual(21, Functions.triangular(6))
        self.assertEqual(28, Functions.triangular(7))
        self.assertEqual(36, Functions.triangular(8))
        self.assertEqual(45, Functions.triangular(9))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
