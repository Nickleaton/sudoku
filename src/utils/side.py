"""Side."""
from enum import Enum
from types import MappingProxyType
from typing import Mapping

from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.direction import Direction
from src.utils.order import Order


class Side(Enum):  # noqa: WPS214
    """Enum representing the sides of a board."""

    TOP = 'T'
    RIGHT = 'R'
    BOTTOM = 'B'
    LEFT = 'L'

    @staticmethod
    def create(letter: str) -> 'Side':
        """Create a Side from a letter.

        Args:
            letter (str): The letter representing the side.

        Returns:
            Side: The corresponding Side enum.
        """
        if not Side.valid(letter):
            raise ValueError(f"Invalid side letter: {letter}")
        return Side(letter)

    @staticmethod
    def valid(letter: str) -> bool:
        """Check if a letter corresponds to a valid Side.

        Args:
            letter (str): The letter to validate.

        Returns:
            bool: True if the letter is valid, False otherwise.
        """
        # noinspection PyProtectedMember
        return letter in Side._value2member_map_

    def direction(self, cyclic: Cyclic) -> Direction:
        """Get the direction corresponding to the side and cyclic order.

        Args:
            cyclic (Cyclic): The cyclic order (CLOCKWISE or ANTICLOCKWISE).

        Returns:
            Direction: The direction corresponding to the side and cyclic order.

        Raises:
            SideException: If the combination is unknown.
        """
        return DIRECTION_MAP[(self, cyclic)]

    def order_direction(self, order: Order) -> Direction:  # pylint: disable=too-many-return-statements
        """Get the direction based on the side and order.

        Args:
            order (Order): The order (INCREASING or DECREASING).

        Returns:
            Direction: The direction corresponding to the side and order.

        Raises:
            SideException: If the combination is unknown.
        """
        return ORDER_DIRECTION_MAP[(self, order)]

    def order_offset(self) -> Coord:  # pylint: disable=too-many-return-statements
        """Get the offset for the order based on the side.

        Returns:
            Coord: The coordinate offset corresponding to the side.

        Raises:
            SideException: If the combination is unknown.
        """
        return ORDER_OFFSET_MAP[self]

    @property
    def horizontal(self) -> bool:
        """Check if the side is horizontal.

        Returns:
            bool: True if the side is horizontal (LEFT or RIGHT), False otherwise.
        """
        return self in {Side.LEFT, Side.RIGHT}

    @property
    def vertical(self) -> bool:
        """Check if the side is vertical.

        Returns:
            bool: True if the side is vertical (TOP or BOTTOM), False otherwise.
        """
        return self in {Side.TOP, Side.BOTTOM}

    @staticmethod
    def values() -> str:
        """Get the string representation of all side values.

        Returns:
            str: A string of all side values.
        """
        return "".join([side.value for side in Side])

    def __repr__(self) -> str:
        """Return the string representation of the Side.

        Returns:
            str: The string representation of the side.
        """
        return f"Side.{self.name}"


DIRECTION_MAP: Mapping[tuple[Side, Cyclic], Direction] = MappingProxyType({
    (Side.TOP, Cyclic.CLOCKWISE): Direction.DOWN_RIGHT,
    (Side.RIGHT, Cyclic.CLOCKWISE): Direction.DOWN_LEFT,
    (Side.BOTTOM, Cyclic.CLOCKWISE): Direction.UP_LEFT,
    (Side.LEFT, Cyclic.CLOCKWISE): Direction.UP_RIGHT,
    (Side.TOP, Cyclic.ANTICLOCKWISE): Direction.DOWN_LEFT,
    (Side.RIGHT, Cyclic.ANTICLOCKWISE): Direction.UP_LEFT,
    (Side.BOTTOM, Cyclic.ANTICLOCKWISE): Direction.UP_RIGHT,
    (Side.LEFT, Cyclic.ANTICLOCKWISE): Direction.DOWN_RIGHT,
})

ORDER_DIRECTION_MAP: Mapping[tuple[Side, Order], Direction] = MappingProxyType({
    (Side.TOP, Order.INCREASING): Direction.DOWN,
    (Side.TOP, Order.DECREASING): Direction.UP,
    (Side.RIGHT, Order.INCREASING): Direction.LEFT,
    (Side.RIGHT, Order.DECREASING): Direction.RIGHT,
    (Side.BOTTOM, Order.INCREASING): Direction.UP,
    (Side.BOTTOM, Order.DECREASING): Direction.DOWN,
    (Side.LEFT, Order.INCREASING): Direction.RIGHT,
    (Side.LEFT, Order.DECREASING): Direction.LEFT,
})

ORDER_OFFSET_MAP: Mapping[Side, Coord] = MappingProxyType({
    Side.TOP: Direction.DOWN.offset,
    Side.RIGHT: Direction.LEFT.offset,
    Side.BOTTOM: Direction.UP.offset,
    Side.LEFT: Direction.RIGHT.offset,
})
