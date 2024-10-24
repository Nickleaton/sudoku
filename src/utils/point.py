"""Class for 2D Points."""

import math
from typing import Tuple

CELL_SIZE = 100


class Point:
    """Represent points on a canvas or a 2D vector."""

    def __init__(self, x: float, y: float):
        """
        Construct a point.

        Args:
            x (float): The x coordinate.
            y (float): The y coordinate.
        """
        self.x: float = x
        self.y: float = y

    @property
    def transform(self) -> str:
        """
        Returns a string for an SVG translation to point.

        Returns:
            str: The SVG translation string.
        """
        return f"translate({round(self.x, 1)}, {round(self.y, 1)})"

    def __add__(self, other: 'Point') -> 'Point':
        """
        Add two points.

        Args:
            other (Point): The point to add.

        Returns:
            Point: The resulting point after addition.
        """
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        """
        Calculate the difference of two points.

        Args:
            other (Point): The point to subtract.

        Returns:
            Point: The resulting point after subtraction.
        """
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> 'Point':
        """
        Scale a point by a scale factor.

        Args:
            other (float): The scale factor.

        Returns:
            Point: The scaled point.
        """
        return Point(self.x * other, self.y * other)

    def __truediv__(self, other: float) -> 'Point':
        """
        Scale a point by dividing by a scale factor.

        Args:
            other (float): The scale factor.

        Returns:
            Point: The scaled point.
        """
        return Point(self.x / other, self.y / other)

    def __neg__(self) -> 'Point':
        """
        Return the negation of a point's coordinates.

        Returns:
            Point: The point with negated coordinates.
        """
        return Point(-self.x, -self.y)

    @property
    def magnitude(self) -> float:
        """
        Return the Pythagorean magnitude of the point.

        Returns:
            float: The magnitude of the point.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def coordinates(self) -> Tuple[float, float]:
        """
        Get the coordinates as an (x, y) tuple.

        Returns:
            Tuple[float, float]: The x and y coordinates.
        """
        return self.x, self.y

    def __repr__(self) -> str:
        """
        Return a string representation of the Point.

        Returns:
            str: The string representation of the point.
        """
        return f"Point({self.x}, {self.y})"
