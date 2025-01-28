import unittest

from src.items.digit import digit08, digit14, digit16, digit19, digit1F


class TestDigit(unittest.TestCase):
    """Base test class for Digit."""

    def setUp(self) -> None:
        """Set up test case with instance-specific minimum and maximum."""
        self.minimum = None
        self.maximum = None
        self.digit = None
        if self.digit is None:
            self.skipTest('Base test class skipped because self.digit is not defined.')

    def test_instance_creation(self) -> None:
        """Test that an instance of Digit is created correctly."""
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


class TestDigit0To8(TestDigit):
    """Test class for Digit(0, 8)."""

    def setUp(self) -> None:
        self.minimum = 0
        self.maximum = 8
        self.digit = digit08


class TestDigit1To4(TestDigit):
    """Test class for Digit(1, 4)."""

    def setUp(self) -> None:
        self.minimum = 1
        self.maximum = 4
        self.digit = digit14


class TestDigit1To6(TestDigit):
    """Test class for Digit(1, 6)."""

    def setUp(self) -> None:
        self.minimum = 1
        self.maximum = 6
        self.digit = digit16


class TestDigit1To9(TestDigit):
    """Test class for Digit(1, 9)."""

    def setUp(self) -> None:
        self.minimum = 1
        self.maximum = 9
        self.digit = digit19


class TestDigit1ToF(TestDigit):
    """Test class for Digit(1, F)."""

    def setUp(self) -> None:
        self.minimum = 1
        self.maximum = 0xF  # Hexadecimal for 15
        self.digit = digit1F


if __name__ == '__main__':
    unittest.main()
