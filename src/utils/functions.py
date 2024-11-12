"""Mathematical functions."""

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)


class Functions:
    """A utility class that provides static mathematical functions."""

    @staticmethod
    def triangular(n: int) -> int:
        """
        Calculate the nth triangular number.

        The nth triangular number is the sum of the integers from 1 to n,
        and can be calculated as n * (n + 1) // 2.

        Args:
            n (int): The number of terms to sum.

        Returns:
            int: The nth triangular number.
        """
        return n * (n + 1) // 2

    @staticmethod
    def prime(n: int) -> int:
        """
        Retrieve the nth prime number from a predefined list.

        Args:
            n (int): The index of the prime number to retrieve (0-based).

        Returns:
            int: The nth prime number from the predefined list.

        Raises:
            IndexError: If n is out of the range of the predefined list.
        """
        if not (0 <= n < len(PRIMES)):
            raise IndexError(f"Index {n} is out of bounds for the prime list.")
        return PRIMES[n]
