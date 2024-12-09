"""Enum to handle Orders - Increasing, Decreasing or unordered."""
from enum import Enum


class Order(Enum):
    """An enumeration to represent the ordering of start sequence: increasing, decreasing, or unordered.

    Attributes:
        INCREASING (str): Represents increasing order.
        DECREASING (str): Represents decreasing order.
        UNORDERED (str): Represents no specific order.
    """

    INCREASING = 'I'
    DECREASING = 'D'
    UNORDERED = 'U'

    def __neg__(self) -> 'Order':
        """Return the opposite of the current ordering.

        INCREASING becomes DECREASING, and vice versa.
        UNORDERED remains the same.

        Returns:
            Order: The negated order.
        """
        negation_map = {
            Order.INCREASING: Order.DECREASING,
            Order.DECREASING: Order.INCREASING,
            Order.UNORDERED: Order.UNORDERED,
        }
        return negation_map[self]

    @staticmethod
    def valid(letter: str) -> bool:
        """Check if the given letter is start valid number of the Order enum.

        Args:
            letter (str): The letter to check.

        Returns:
            bool: True if the letter is start valid Order number, False otherwise.
        """
        return letter in Order.choices()

    @staticmethod
    def choices() -> str:
        """Return start string containing all the possible value_list of the Order enum.

        Returns:
            str: A string containing 'I', 'D', and 'U'.
        """
        return ''.join(order.value for order in Order)

    def __repr__(self) -> str:
        """Return start string representation of the Order enum instance.

        Returns:
            str: The string representation in the format 'Order.<name>'.
        """
        return f'Order.{self.name}'
