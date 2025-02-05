import unittest

from src.board.digits import Digits


class TestDigits(unittest.TestCase):
    """Base test class for Digits."""

    def setUp(self) -> None:
        """Set up test case with instance-specific minimum and maximum."""
        self.minimum = None
        self.maximum = None
        self.digit = None
        self.count = None
        self.digit_sum = None
        self.representation = None
        self.representation = None
        self.odd = None
        self.even = None
        self.low = None
        self.mid = None
        self.high = None
        self.mod0 = None
        self.mod1 = None
        self.mod2 = None
        self.prime = None
        if self.digit is None:
            self.skipTest('Base test class skipped because self.digit is not defined.')

    def test_count(self):
        """Test the count of the digit range."""
        self.assertEqual(self.count, self.digit.count)
        self.assertEqual(self.count, len(self.digit.digit_range))

    def test_digit_sum(self):
        """Test the sum of the digit range."""
        self.assertEqual(self.digit_sum, self.digit.digit_sum)
        self.assertEqual(self.digit_sum, sum(self.digit.digit_range))

    def test_representation(self) -> None:
        """Test the string representation of the Digits instance."""
        self.assertEqual(repr(self.digit), self.representation)

    def test_instance_creation(self) -> None:
        """Test that an instance of Digits is created correctly."""
        self.assertIsNotNone(self.digit)
        self.assertEqual(self.digit.minimum, self.minimum)
        self.assertEqual(self.digit.maximum, self.maximum)

    def test_len(self) -> None:
        """Test the length of the digit range."""
        expected_length = self.maximum - self.minimum + 1
        self.assertEqual(len(self.digit), expected_length)

    def test_iter(self) -> None:
        """Test iterating over the digit range."""
        expected_range = list(range(self.minimum, self.maximum + 1))
        self.assertEqual(list(self.digit), expected_range)

    def test_contains(self) -> None:
        """Test the `in` operator for the digit range."""
        for value in range(self.minimum, self.maximum + 1):
            self.assertIn(value, self.digit)
        self.assertNotIn(self.minimum - 1, self.digit)
        self.assertNotIn(self.maximum + 1, self.digit)

    def test_is_valid(self) -> None:
        """Test the is_valid method for the digit range."""
        for value in range(self.minimum, self.maximum + 1):
            self.assertTrue(self.digit.is_valid(value))
        self.assertFalse(self.digit.is_valid(self.minimum - 1))
        self.assertFalse(self.digit.is_valid(self.maximum + 1))

    def test_odd_digits(self) -> None:
        """Test the odd digits in the digit range."""
        self.assertEqual([d for d in self.digit if d % 2 != 0], self.odd)

    def test_even_digits(self) -> None:
        """Test the even digits in the digit range."""
        self.assertEqual([d for d in self.digit if d % 2 == 0], self.even)

    def test_low_mid_high(self) -> None:
        """Test the low, mid, and high ranges."""
        if self.low is None:
            return
        self.assertEqual(self.digit.low, self.low)
        self.assertEqual(self.digit.mid, self.mid)
        self.assertEqual(self.digit.high, self.high)

    def test_mod_groups(self) -> None:
        """Test digits grouped by modulus 3."""
        if self.mod0 is None:
            return
        self.assertEqual(self.digit.mod0, self.mod0)
        self.assertEqual(self.digit.mod1, self.mod1)
        self.assertEqual(self.digit.mod2, self.mod2)

    def test_prime_numbers(self) -> None:
        """Test the prime numbers in the digit range."""
        self.assertEqual(self.prime, self.digit.primes)

    def test_lower(self) -> None:
        """Test the lower and upper halves of the digit range."""
        self.assertEqual(self.lower, self.digit.lower)

    def test_upper(self) -> None:
        """Test the lower and upper halves of the digit range."""
        self.assertEqual(self.upper, self.digit.upper)

    def test_wrong_way(self) -> None:
        """Test min > max"""
        with self.assertRaises(ValueError):
            Digits(2, 1)


class TestDigit0To8(TestDigits):
    """Test class for Digits(0, 8)."""

    def setUp(self) -> None:
        self.minimum = 0
        self.maximum = 8
        self.count = 9
        self.digit_sum = 36
        self.digit = Digits(0, 8)
        self.representation = 'Digits(0, 8)'
        self.odd = [1, 3, 5, 7]
        self.even = [0, 2, 4, 6, 8]
        self.low = None
        self.mid = None
        self.high = None
        self.mod0 = None
        self.mod1 = None
        self.mod2 = None
        self.prime = [2, 3, 5, 7]
        self.lower = [0, 1, 2, 3]
        self.upper = [5, 6, 7, 8]


class TestDigit1To8(TestDigits):
    """Test class for Digits(1, 8)."""

    def setUp(self) -> None:
        self.minimum = 1
        self.maximum = 8
        self.count = 8
        self.digit_sum = 36
        self.digit = Digits(1, 8)
        self.representation = 'Digits(1, 8)'
        self.odd = [1, 3, 5, 7]
        self.even = [2, 4, 6, 8]
        self.low = None
        self.mid = None
        self.high = None
        self.mod0 = None
        self.mod1 = None
        self.mod2 = None
        self.prime = [2, 3, 5, 7]
        self.lower = [1, 2, 3, 4]
        self.upper = [5, 6, 7, 8]


class TestDigit1To4(TestDigits):
    """Test class for Digits(1, 4)."""

    def setUp(self) -> None:
        self.minimum = 1
        self.maximum = 4
        self.count = 4
        self.digit_sum = 10
        self.digit = Digits(1, 4)
        self.representation = 'Digits(1, 4)'
        self.odd = [1, 3]
        self.even = [2, 4]
        self.low = None
        self.mid = None
        self.high = None
        self.mod0 = None
        self.mod1 = None
        self.mod2 = None
        self.prime = [2, 3]
        self.lower = [1, 2]
        self.upper = [3, 4]


class TestDigit1To6(TestDigits):
    """Test class for Digits(1, 6)."""

    def setUp(self) -> None:
        self.minimum = 1
        self.maximum = 6
        self.count = 6
        self.digit_sum = 21
        self.digit = Digits(1, 6)
        self.representation = 'Digits(1, 6)'
        self.odd = [1, 3, 5]
        self.even = [2, 4, 6]
        self.low = [1, 2]
        self.mid = [3, 4]
        self.high = [5, 6]
        self.mod0 = [3, 6]
        self.mod1 = [1, 4]
        self.mod2 = [2, 5]
        self.prime = [2, 3, 5]
        self.lower = [1, 2, 3]
        self.upper = [4, 5, 6]


class TestDigit1To9(TestDigits):
    """Test class for Digits(1, 9)."""

    def setUp(self) -> None:
        self.minimum = 1
        self.maximum = 9
        self.count = 9
        self.digit = Digits(1, 9)
        self.digit_sum = 45
        self.representation = 'Digits(1, 9)'
        self.odd = [1, 3, 5, 7, 9]
        self.even = [2, 4, 6, 8]
        self.low = [1, 2, 3]
        self.mid = [4, 5, 6]
        self.high = [7, 8, 9]
        self.mod0 = [3, 6, 9]
        self.mod1 = [1, 4, 7]
        self.mod2 = [2, 5, 8]
        self.prime = [2, 3, 5, 7]
        self.lower = [1, 2, 3, 4]
        self.upper = [6, 7, 8, 9]


class TestDigit1ToF(TestDigits):
    """Test class for Digits(1, F)."""

    def setUp(self) -> None:
        self.minimum = 1
        self.maximum = 16
        self.count = 16
        self.digit_sum = 136
        self.digit = Digits(1, 16)
        self.representation = 'Digits(1, 16)'
        self.odd = [1, 3, 5, 7, 9, 11, 13, 15]
        self.even = [2, 4, 6, 8, 10, 12, 14, 16]
        self.low = None
        self.mid = None
        self.high = None
        self.mod0 = None
        self.mod1 = None
        self.mod2 = None
        self.prime = [2, 3, 5, 7, 11, 13]
        self.lower = [1, 2, 3, 4, 5, 6, 7, 8]
        self.upper = [9, 10, 11, 12, 13, 14, 15, 16]


if __name__ == '__main__':
    unittest.main()
