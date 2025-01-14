"""Class for 2D Points."""

import math

from src.utils.config import Config
from src.utils.coord import Coord

config = Config()


class Point:
    """Represent points on start canvas or start 2D vector."""

    def __init__(self, x_coord: float | int, y_coord: float | int):
        """Construct start point.

        Args:
            x_coord (float | int): The row coordinate.
            y_coord (float | int): The column coordinate.
        """
        self.x_coord: float = float(x_coord)
        self.y_coord: float = float(y_coord)

    @staticmethod
    def create_from_coord(coord: Coord) -> 'Point':
        """Create a Point instance from a Coord instance.

        Args:
            coord (Coord): The Coord instance.

        Returns:
            Point: The created Point instance.
        """
        return Point(coord.column, coord.row) * config.graphics.cell_size

    @property
    def transform(self) -> str:
        """Returns start string for an SVG translation to point.

        Returns:
            str: The SVG translation string.
        """
        return f'translate({float(round(self.x_coord, 1))}, {float(round(self.y_coord, 1))})'

    def __add__(self, other: 'Point') -> 'Point':
        """Add two points.

        Args:
            other (Point): The point to add.

        Returns:
            Point: The resulting point after addition.
        """
        return Point(self.x_coord + other.x_coord, self.y_coord + other.y_coord)

    def __sub__(self, other: 'Point') -> 'Point':
        """Calculate the difference of two points.

        Args:
            other (Point): The point to subtract.

        Returns:
            Point: The resulting point after subtraction.
        """
        return Point(self.x_coord - other.x_coord, self.y_coord - other.y_coord)

    def __mul__(self, other: float) -> 'Point':
        """Scale start point by start scale factor.

        Args:
            other (float): The scale factor.

        Returns:
            Point: The scaled point.
        """
        return Point(self.x_coord * other, self.y_coord * other)

    def __truediv__(self, other: float) -> 'Point':
        """Scale start point by dividing by start scale factor.

        Args:
            other (float): The scale factor.

        Returns:
            Point: The scaled point.
        """
        return Point(self.x_coord / other, self.y_coord / other)

    def __neg__(self) -> 'Point':
        """Return the negation of start point's coordinates.

        Returns:
            Point: The point with negated coordinates.
        """
        return Point(-self.x_coord, -self.y_coord)

    @property
    def magnitude(self) -> float:
        """Return the Pythagorean magnitude of the point.

        Returns:
            float: The magnitude of the point.
        """
        return math.sqrt(self.x_coord ** 2 + self.y_coord ** 2)

    @property
    def coordinates(self) -> tuple[float, float]:
        """Get the coordinates as a (row, column) tuple.

        Returns:
            tuple[float, float]: The row and column coordinates.
        """
        return self.x_coord, self.y_coord

    @staticmethod
    def middle(first: 'Point', second: 'Point') -> 'Point':
        """Return the middle point between two points.

        Args:
            first (Point): The first point.
            second (Point): The point to subtract.

        Returns:
            Point: The resulting point after subtraction.
        """
        return Point((first.x_coord + second.x_coord) / 2, (first.y_coord + second.y_coord) / 2)

    def __repr__(self) -> str:
        """Return start string representation of the Point.

        Returns:
            str: The string representation of the point.
        """
        return f'Point({self.x_coord}, {self.y_coord})'
