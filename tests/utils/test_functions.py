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

    def test_prime(self):
        self.assertEqual(2, Functions.prime(0))
        self.assertEqual(3, Functions.prime(1))
        self.assertEqual(5, Functions.prime(2))
        self.assertEqual(7, Functions.prime(3))
        self.assertEqual(97, Functions.prime(24))  # Testing the last prime in the list

        # Test out of bounds
        with self.assertRaises(IndexError):
            Functions.prime(-1)  # Negative index
        with self.assertRaises(IndexError):
            Functions.prime(25)  # Index out of range


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
