"""Class for 2d Points."""

import math
from typing import Tuple

CELL_SIZE = 100


class Point:
    """Represent points on a canvas or a 2D vector."""

    def __init__(self, x: float, y: float):
        """
        Construct a point.

        :param x: float of the x coordinate
        :param y: float of the y coordinate
        """
        self.x: float = x
        self.y: float = y

    @property
    def transform(self) -> str:
        """
        Returns a string for a SVG translation to point.

        :return: str
        """
        return f"translate({round(self.x, 1)}, {round(self.y, 1)})"

    def __add__(self, other: 'Point') -> 'Point':
        """
        Add two points.

        :param other:
        :return: Point
        """
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        """
        Difference of two points.

        :param other:
        :return: Point
        """
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> 'Point':
        """
        Scale a point by a scale factor.

        :param other: scale
        :return: Point
        """
        return Point(self.x * other, self.y * other)

    def __truediv__(self, other: float) -> 'Point':
        """
        Scale a point by dividing by a  scale factor.

        :param other: scale
        :return: Point
        """
        return Point(self.x / other, self.y / other)

    def __neg__(self) -> 'Point':
        """
        Return the negation of a point's coordinates.

        :return: Point
        """
        return Point(-self.x, -self.y)

    @property
    def magnitude(self) -> float:
        """
        Return the Pythagorean magnitude of a point.

        :return:  float
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def coordinates(self) -> Tuple[float, float]:
        """
        Get the coordinates as an x,y tuple.

        :return: Tuple.
        """
        return self.x, self.y

    def __repr__(self) -> str:
        """
        Representation of a Point.

        :return: str
        """
        return f"Point({self.x}, {self.y})"
