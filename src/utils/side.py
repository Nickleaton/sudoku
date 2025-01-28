"""Side."""

from enum import StrEnum
from types import MappingProxyType
from typing import Mapping

from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.moves import Moves
from src.utils.order import Order


class Side(StrEnum):
    """Enum representing the sides of a starting board (top, right, bottom, left)."""

    top = 'T'
    right = 'R'
    bottom = 'B'
    left = 'L'

    @staticmethod
    def create(letter: str) -> 'Side':
        """Create a Side enum from a letter representing a side.

        Args:
            letter (str): The letter representing a side ('T', 'R', 'B', or 'L').

        Returns:
            Side: The corresponding Side enum.

        Raises:
            ValueError: If the letter does not correspond to a valid side.
        """
        if not Side.valid(letter):
            raise ValueError(f'Invalid side letter: {letter}. Valid options are: {Side.choices()}')
        return Side(letter)

    @staticmethod
    def valid(letter: str) -> bool:
        """Check if the letter corresponds to a valid Side.

        Args:
            letter (str): The letter to validate ('T', 'R', 'B', or 'L').

        Returns:
            bool: True if the letter is valid, False otherwise.
        """
        return letter in {side.value for side in Side}

    def direction(self, cyclic: Cyclic) -> Coord:
        """Get the direction corresponding to the side and cyclic order.

        Args:
            cyclic (Cyclic): The cyclic order (clockwise or anticlockwise).

        Returns:
            Coord: The direction corresponding to the side and cyclic order.
        """
        return DIRECTION_MAP[(self, cyclic)]

    def order_direction(self, order: Order) -> Coord:
        """Get the direction based on the side and order (increasing or decreasing).

        Args:
            order (Order): The order (increasing or decreasing).

        Returns:
            Coord: The direction corresponding to the side and order.
        """
        return ORDER_DIRECTION_MAP[(self, order)]

    def order_offset(self) -> Coord:
        """Get the coordinate offset for the order based on the side.

        Returns:
            Coord: The coordinate offset corresponding to the side.
        """
        return ORDER_OFFSET_MAP[self]

    @property
    def horizontal(self) -> bool:
        """Check if the side is horizontal.

        Returns:
            bool: True if the side is horizontal, False otherwise.
        """
        return self in {Side.left, Side.right}

    @property
    def vertical(self) -> bool:
        """Check if the side is vertical.

        Returns:
            bool: True if the side is vertical, False otherwise.
        """
        return self in {Side.top, Side.bottom}

    @staticmethod
    def choices() -> str:
        """Get a string representation of all side value_list.

        Returns:
            str: A string of all side value_list (exp.g., 'TRBL' for top, right, bottom, left).
        """
        return ''.join(side.value for side in Side)

    def __repr__(self) -> str:
        """Return the string representation of the Side.

        Returns:
            str: The string representation of the side (exp.g., 'Side.top').
        """
        return f'Side.{self.name}'


# Mappings for directions, orders, and offsets.
DIRECTION_MAP: Mapping[tuple[Side, Cyclic], Coord] = MappingProxyType({
    (Side.top, Cyclic.clockwise): Moves.down_right,
    (Side.right, Cyclic.clockwise): Moves.down_left,
    (Side.bottom, Cyclic.clockwise): Moves.up_left,
    (Side.left, Cyclic.clockwise): Moves.up_right,
    (Side.top, Cyclic.anticlockwise): Moves.down_left,
    (Side.right, Cyclic.anticlockwise): Moves.up_left,
    (Side.bottom, Cyclic.anticlockwise): Moves.up_right,
    (Side.left, Cyclic.anticlockwise): Moves.down_right,
})

ORDER_DIRECTION_MAP: Mapping[tuple[Side, Order], Coord] = MappingProxyType({
    (Side.top, Order.increasing): Moves.down,
    (Side.top, Order.decreasing): Moves.up,
    (Side.right, Order.increasing): Moves.left,
    (Side.right, Order.decreasing): Moves.right,
    (Side.bottom, Order.increasing): Moves.up,
    (Side.bottom, Order.decreasing): Moves.down,
    (Side.left, Order.increasing): Moves.right,
    (Side.left, Order.decreasing): Moves.left,
})

ORDER_OFFSET_MAP: Mapping[Side, Coord] = MappingProxyType({
    Side.top: Moves.down,
    Side.right: Moves.left,
    Side.bottom: Moves.up,
    Side.left: Moves.right,
})
