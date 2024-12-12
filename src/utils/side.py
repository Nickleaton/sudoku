"""Side."""

from enum import StrEnum
from types import MappingProxyType
from typing import Mapping

from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.moves import Moves
from src.utils.order import Order


class Side(StrEnum):
    """Enum representing the sides of a starting board (TOP, RIGHT, BOTTOM, LEFT)."""

    TOP = 'T'
    RIGHT = 'R'
    BOTTOM = 'B'
    LEFT = 'L'

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
            cyclic (Cyclic): The cyclic order (CLOCKWISE or ANTICLOCKWISE).

        Returns:
            Coord: The direction corresponding to the side and cyclic order.
        """
        return DIRECTION_MAP[(self, cyclic)]

    def order_direction(self, order: Order) -> Coord:
        """Get the direction based on the side and order (INCREASING or DECREASING).

        Args:
            order (Order): The order (INCREASING or DECREASING).

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
        return self in {Side.LEFT, Side.RIGHT}

    @property
    def vertical(self) -> bool:
        """Check if the side is vertical.

        Returns:
            bool: True if the side is vertical, False otherwise.
        """
        return self in {Side.TOP, Side.BOTTOM}

    @staticmethod
    def choices() -> str:
        """Get a string representation of all side value_list.

        Returns:
            str: A string of all side value_list (e.g., 'TRBL' for TOP, RIGHT, BOTTOM, LEFT).
        """
        return ''.join(side.value for side in Side)

    def __repr__(self) -> str:
        """Return the string representation of the Side.

        Returns:
            str: The string representation of the side (e.g., 'Side.TOP').
        """
        return f'Side.{self.name}'


# Mappings for directions, orders, and offsets.
DIRECTION_MAP: Mapping[tuple[Side, Cyclic], Coord] = MappingProxyType({
    (Side.TOP, Cyclic.CLOCKWISE): Moves.DOWN_RIGHT,
    (Side.RIGHT, Cyclic.CLOCKWISE): Moves.DOWN_LEFT,
    (Side.BOTTOM, Cyclic.CLOCKWISE): Moves.UP_LEFT,
    (Side.LEFT, Cyclic.CLOCKWISE): Moves.UP_RIGHT,
    (Side.TOP, Cyclic.ANTICLOCKWISE): Moves.DOWN_LEFT,
    (Side.RIGHT, Cyclic.ANTICLOCKWISE): Moves.UP_LEFT,
    (Side.BOTTOM, Cyclic.ANTICLOCKWISE): Moves.UP_RIGHT,
    (Side.LEFT, Cyclic.ANTICLOCKWISE): Moves.DOWN_RIGHT,
})

ORDER_DIRECTION_MAP: Mapping[tuple[Side, Order], Coord] = MappingProxyType({
    (Side.TOP, Order.INCREASING): Moves.DOWN,
    (Side.TOP, Order.DECREASING): Moves.UP,
    (Side.RIGHT, Order.INCREASING): Moves.LEFT,
    (Side.RIGHT, Order.DECREASING): Moves.RIGHT,
    (Side.BOTTOM, Order.INCREASING): Moves.UP,
    (Side.BOTTOM, Order.DECREASING): Moves.DOWN,
    (Side.LEFT, Order.INCREASING): Moves.RIGHT,
    (Side.LEFT, Order.DECREASING): Moves.LEFT,
})

ORDER_OFFSET_MAP: Mapping[Side, Coord] = MappingProxyType({
    Side.TOP: Moves.DOWN,
    Side.RIGHT: Moves.LEFT,
    Side.BOTTOM: Moves.UP,
    Side.LEFT: Moves.RIGHT,
})
