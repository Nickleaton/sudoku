import unittest

from src.board.digits import Digits


class TestDigits(unittest.TestCase):
    """Base test class for Digits."""

    minimum = None
    maximum = None

    def setUp(self) -> None:
        """Set up test case with instance-specific minimum and maximum."""
        if self.minimum is None or self.maximum is None:
            self.skipTest('Base test class skipped because minimum and maximum are not defined.')

        self.digits = Digits(self.minimum, self.maximum)
        self.digits_sum = sum(range(self.minimum, self.maximum + 1))
        self.representation = f'Digits({self.minimum}, {self.maximum})'
        self.count = self.maximum - self.minimum + 1
        self.odd = [i for i in range(self.minimum, self.maximum + 1) if i % 2 != 0]
        self.even = [i for i in range(self.minimum, self.maximum + 1) if i % 2 == 0]
        self.prime = self.get_primes(self.minimum, self.maximum)
        # Adjust for odd count of digits
        half = self.count // 2
        self.lower = list(range(self.minimum, self.minimum + half))
        self.upper = list(range(self.minimum + half + self.count % 2, self.maximum + 1))

    @staticmethod
    def is_prime(num):
        """Helper method to check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(self, start, end):
        """Helper method to calculate prime numbers within a given range."""
        return [num for num in range(start, end + 1) if self.is_prime(num)]

    def test_count(self):
        """Test the count of the digit range."""
        self.assertEqual(self.count, self.digits.count)
        self.assertEqual(self.count, len(self.digits.digit_range))

    def test_digit_sum(self):
        """Test the sum of the digit range."""
        self.assertEqual(self.digits_sum, self.digits.digit_sum)
        self.assertEqual(self.digits_sum, sum(self.digits.digit_range))

    def test_representation(self) -> None:
        """Test the string representation of the Digits instance."""
        self.assertEqual(repr(self.digits), self.representation)

    def test_instance_creation(self) -> None:
        """Test that an instance of Digits is created correctly."""
        self.assertIsNotNone(self.digits)
        self.assertEqual(self.digits.minimum, self.minimum)
        self.assertEqual(self.digits.maximum, self.maximum)

    def test_len(self) -> None:
        """Test the length of the digit range."""
        expected_length = self.maximum - self.minimum + 1
        self.assertEqual(len(self.digits), expected_length)

    def test_iter(self) -> None:
        """Test iterating over the digit range."""
        expected_range = list(range(self.minimum, self.maximum + 1))
        self.assertEqual(list(self.digits), expected_range)

    def test_contains(self) -> None:
        """Test the `in` operator for the digit range."""
        for value in range(self.minimum, self.maximum + 1):
            self.assertIn(value, self.digits)
        self.assertNotIn(self.minimum - 1, self.digits)
        self.assertNotIn(self.maximum + 1, self.digits)

    def test_is_valid(self) -> None:
        """Test the is_valid method for the digit range."""
        for value in range(self.minimum, self.maximum + 1):
            self.assertTrue(self.digits.is_valid(value))
        self.assertFalse(self.digits.is_valid(self.minimum - 1))
        self.assertFalse(self.digits.is_valid(self.maximum + 1))

    def test_odd_digits(self) -> None:
        """Test the odd digits in the digit range."""
        self.assertEqual([d for d in self.digits if d % 2 != 0], self.odd)

    def test_even_digits(self) -> None:
        """Test the even digits in the digit range."""
        self.assertEqual([d for d in self.digits if d % 2 == 0], self.even)

    def test_prime_numbers(self) -> None:
        """Test the prime numbers in the digit range."""
        self.assertEqual(self.prime, self.digits.primes)

    def test_lower(self) -> None:
        """Test the lower half of the digit range."""
        self.assertEqual(self.lower, self.digits.lower)

    def test_upper(self) -> None:
        """Test the upper half of the digit range."""
        self.assertEqual(self.upper, self.digits.upper)

    def test_wrong_way(self) -> None:
        """Test min > max"""
        with self.assertRaises(ValueError):
            Digits(2, 1)


class TestDigit0To8(TestDigits):
    """Test class for Digits(0, 8)."""

    minimum = 0
    maximum = 8


class TestDigit1To8(TestDigits):
    """Test class for Digits(1, 8)."""

    minimum = 1
    maximum = 8


class TestDigit1To4(TestDigits):
    """Test class for Digits(1, 4)."""

    minimum = 1
    maximum = 4


class TestDigit1To6(TestDigits):
    """Test class for Digits(1, 6)."""

    minimum = 1
    maximum = 6


class TestDigit1To9(TestDigits):
    """Test class for Digits(1, 9)."""

    minimum = 1
    maximum = 9


class TestDigit1ToF(TestDigits):
    """Test class for Digits(1, 16)."""

    minimum = 1
    maximum = 16


if __name__ == '__main__':
    unittest.main()
