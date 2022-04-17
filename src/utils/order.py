from enum import Enum


class OrderException(Exception):
    pass


class Order(Enum):
    INCREASING = 'I'
    DECREASING = 'D'

    def __neg__(self) -> 'Order':
        if self == Order.INCREASING:
            return Order.DECREASING
        if self == Order.DECREASING:
            return Order.INCREASING
        raise OrderException('Unknown Order')  # pragma: no cover

    @staticmethod
    def create(letter: str) -> 'Order':
        if letter == 'I':
            return Order.INCREASING
        if letter == 'D':
            return Order.DECREASING
        raise OrderException(f"Unknown order letter {letter}")

    def __repr__(self) -> str:
        return f"Order.{self.name}"
