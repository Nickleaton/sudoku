from enum import Enum


class Order(Enum):
    INCREASING = 'I'
    DECREASING = 'D'
    UNORDERED = 'U'

    def __neg__(self) -> 'Order':
        negation_map = {
            Order.INCREASING: Order.DECREASING,
            Order.DECREASING: Order.INCREASING,
            Order.UNORDERED: Order.UNORDERED
        }
        return negation_map[self]

    @staticmethod
    def valid(letter: str) -> bool:
        return letter in Order.values()

    @staticmethod
    def values() -> str:
        return "".join(order.value for order in Order)

    def __repr__(self) -> str:
        return f"Order.{self.name}"

