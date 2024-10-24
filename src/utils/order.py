from enum import Enum


class Order(Enum):
    """
    An enumeration to represent the ordering of a sequence: increasing, decreasing, or unordered.

    Attributes:
        INCREASING (str): Represents increasing order.
        DECREASING (str): Represents decreasing order.
        UNORDERED (str): Represents no specific order.
    """

    INCREASING = 'I'
    DECREASING = 'D'
    UNORDERED = 'U'

    def __neg__(self) -> 'Order':
        """
        Returns the opposite of the current ordering.
        INCREASING becomes DECREASING, and vice versa.
        UNORDERED remains the same.

        Returns:
            Order: The negated order.
        """
        negation_map = {
            Order.INCREASING: Order.DECREASING,
            Order.DECREASING: Order.INCREASING,
            Order.UNORDERED: Order.UNORDERED
        }
        return negation_map[self]

    @staticmethod
    def valid(letter: str) -> bool:
        """
        Checks if the given letter is a valid value of the Order enum.

        Args:
            letter (str): The letter to check.

        Returns:
            bool: True if the letter is a valid Order value, False otherwise.
        """
        return letter in Order.values()

    @staticmethod
    def values() -> str:
        """
        Returns a string containing all the possible values of the Order enum.

        Returns:
            str: A string containing 'I', 'D', and 'U'.
        """
        return "".join(order.value for order in Order)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Order enum instance.

        Returns:
            str: The string representation in the format 'Order.<name>'.
        """
        return f"Order.{self.name}"
