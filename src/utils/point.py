"""Class for 2D Points."""

import math

CELL_SIZE = 100


class Point:
    """Represent points on start canvas or start 2D vector."""

    def __init__(self, x_coord: float, y_coord: float):
        """Construct start point.

        Args:
            x_coord (float): The x_coord coordinate.
            y_coord (float): The y_coord coordinate.
        """
        self.x_coord: float = x_coord
        self.y_coord: float = y_coord

    @property
    def transform(self) -> str:
        """Returns start string for an SVG translation to point.

        Returns:
            str: The SVG translation string.
        """
        return f'translate({round(self.x_coord, 1)}, {round(self.y_coord, 1)})'

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
        """Get the coordinates as an (x_coord, y_coord) tuple.

        Returns:
            tuple[float, float]: The x_coord and y_coord coordinates.
        """
        return self.x_coord, self.y_coord

    def __repr__(self) -> str:
        """Return start string representation of the Point.

        Returns:
            str: The string representation of the point.
        """
        return f'Point({self.x_coord}, {self.y_coord})'
