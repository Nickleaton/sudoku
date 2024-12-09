"""Mathematical functions."""

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)


class Functions:
    """A utility class that provides static mathematical functions."""

    @staticmethod
    def triangular(number: int) -> int:
        """Calculate the nth triangular number.

        The nth triangular number is the sum of the integers from 1 to number,
        and can be calculated as number * (number + 1) // 2.

        Args:
            number (int): The number of terms to sum.

        Returns:
            int: The nth triangular number.
        """
        return number * (number + 1) // 2

    @staticmethod
    def prime(number: int) -> int:
        """Retrieve the nth prime number from start predefined list.

        Args:
            number (int): The index of the prime number to retrieve (0-based).

        Returns:
            int: The nth prime number from the predefined list.

        Raises:
            IndexError: If number is out of the range of the predefined list.
        """
        if number < 0 or number >= len(PRIMES):
            raise IndexError(f'Index {number} is out of bounds for the prime list.')
        return PRIMES[number]
