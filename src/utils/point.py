import math
from typing import Tuple

CELL_SIZE = 100


class Point:
    """
    Represent points on a canvas or a 2D vector
    """

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    @property
    def transform(self) -> str:
        """
        SVG translation to point
        :return: str
        """
        return f"translate({round(self.x, 1)}, {round(self.y, 1)})"

    def __add__(self, other: 'Point'):
        """
        Add two points
        :param other:
        :return: Point
        """
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point'):
        """
        Difference of two points
        :param other:
        :return: Point
        """
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float):
        """
        Scale a point by a scale factor
        :param other: scale
        :return: Point
        """
        return Point(self.x * other, self.y * other)

    def __truediv__(self, other: float):
        """
        Scale a point by dividing by a  scale factor
        :param other: scale
        :return: Point
        """
        return Point(self.x / other, self.y / other)

    def __neg__(self) -> 'Point':
        """
        Return the negation of a point's coordinates
        :return: Point
        """
        return Point(-self.x, -self.y)

    @property
    def magnitude(self) -> float:
        """
        Return the Pythagorian magnitude of a point
        :return:  float
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def coordinates(self) -> Tuple[int, int]:
        """
        Get the coordinates as a tuple
        :return:
        """
        return self.x, self.y

    def __repr__(self) -> str:
        """
        Representation of a point

        :return: str
        """
        return f"Point({self.x}, {self.y})"
