# pylint: disable=too-few-public-methods
class Functions:
    """
    A utility class that contains static mathematical functions.
    """

    @staticmethod
    def triangular(n: int) -> int:
        """
        Returns the nth triangular number.

        The nth triangular number is the sum of the integers from 1 to n.

        Args:
            n (int): The number of terms to sum.

        Returns:
            int: The nth triangular number, calculated as n * (n + 1) // 2.
        """
        return n * (n + 1) // 2
