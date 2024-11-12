"""Enum to handle Orders - Increasing, Decreasing or unoredered."""
from enum import Enum
from typing import Dict


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
        Return the opposite of the current ordering.

        INCREASING becomes DECREASING, and vice versa.
        UNORDERED remains the same.

        Returns:
            Order: The negated order.
        """
        return NEGATION_MAP[self]

    @staticmethod
    def valid(letter: str) -> bool:
        """
        Check if the given letter is a valid value of the Order enum.

        Args:
            letter (str): The letter to check.

        Returns:
            bool: True if the letter is a valid Order value, False otherwise.
        """
        return letter in Order.values()

    @staticmethod
    def values() -> str:
        """
        Return a string containing all the possible values of the Order enum.

        Returns:
            str: A string containing 'I', 'D', and 'U'.
        """
        return "".join(order.value for order in Order)

    def __repr__(self) -> str:
        """
        Return a string representation of the Order enum instance.

        Returns:
            str: The string representation in the format 'Order.<name>'.
        """
        return f"Order.{self.name}"

# Map to handle negation of Order
NEGATION_MAP: Dict[Order, Order] = {
    Order.INCREASING: Order.DECREASING,
    Order.DECREASING: Order.INCREASING,
    Order.UNORDERED: Order.UNORDERED
}
