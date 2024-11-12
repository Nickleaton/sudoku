"""Coordinate."""
from typing import List
from src.utils.point import Point
from src.utils.sudoku_exception import SudokuException


class CoordException(SudokuException):
    """Custom exception for Coord operations."""


class Coord:
    """
    Class to represent a coordinate on a Sudoku grid.

    Args:
        row (float): The row value of the coordinate.
        column (float): The column value of the coordinate.
    """

    def __init__(self, row: float, column: float):
        """Initialize a Coord instance.

        Args:
            row (float): The row value of the coordinate.
            column (float): The column value of the coordinate.
        """
        self.row = row
        self.column = column

    def __repr__(self) -> str:
        """
        Return a string representation of the Coord object.

        Returns:
            str: The string representation of the Coord.
        """
        return f"{self.__class__.__name__}({repr(self.row)}, {repr(self.column)})"

    def __add__(self, other: 'Coord') -> 'Coord':
        """
        Add two Coord objects.

        Args:
            other (Coord): The other Coord object to add.

        Returns:
            Coord: A new Coord object that is the sum of the two coordinates.
        """
        return Coord(self.row + other.row, self.column + other.column)

    def __sub__(self, other: 'Coord') -> 'Coord':
        """
        Subtract one Coord object from another.

        Args:
            other (Coord): The Coord object to subtract.

        Returns:
            Coord: A new Coord object that is the difference between the two coordinates.
        """
        return Coord(self.row - other.row, self.column - other.column)

    def __mul__(self, other: object) -> 'Coord':
        """
        Multiply a Coord by another Coord or a scalar (int or float).

        Args:
            other (object): The other object (Coord, int, or float) to multiply by.

        Returns:
            Coord: A new Coord object after multiplication.

        Raises:
            CoordException: If the other object is not a Coord, int, or float.
        """
        if isinstance(other, Coord):
            return Coord(self.row * other.row, self.column * other.column)
        if isinstance(other, (int, float)):
            return Coord(self.row * other, self.column * other)
        raise CoordException(f"Multiplication not supported for Coord and {type(other)}")

    def __truediv__(self, other: float | int) -> 'Coord':
        """
        Divide a Coord by a scalar.

        Args:
            other (float | int): The scalar to divide by.

        Returns:
            Coord: A new Coord object after division.
        """
        return Coord(self.row / other, self.column / other)

    def __neg__(self) -> 'Coord':
        """
        Negate a Coord.

        Returns:
            Coord: A new Coord object with negated row and column values.
        """
        return Coord(-self.row, -self.column)

    def __eq__(self, other: object) -> bool:
        """
        Check if two Coord objects are equal.

        Args:
            other (object): The other object to compare.

        Returns:
            bool: True if the coordinates are equal, False otherwise.

        Raises:
            CoordException: If the other object is not a Coord.
        """
        if isinstance(other, Coord):
            return (self.row == other.row) and (self.column == other.column)
        raise CoordException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __lt__(self, other: object) -> bool:
        """
        Check if this Coord is less than another Coord based on row and column values.

        Args:
            other (object): The other object to compare.

        Returns:
            bool: True if this Coord is less than the other Coord.

        Raises:
            CoordException: If the other object is not a Coord.
        """
        if isinstance(other, Coord):
            if self.row < other.row:
                return True
            if self.row == other.row:
                return self.column < other.column
            return False
        raise CoordException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    @staticmethod
    def validate(yaml) -> List[str]:
        """
        Validate a list containing row and column values.

        Args:
            yaml: The input list to validate.

        Returns:
            List[str]: A list of error messages if validation fails, otherwise an empty list.
        """
        result = []
        if not isinstance(yaml, list):
            result.append(f"Expecting list, got {yaml!r}")
            return result
        if len(yaml) != 2:
            result.append("expecting row, column")
        if not isinstance(yaml[0], int):
            result.append("row not int")
        if not isinstance(yaml[1], int):
            result.append("column not int")
        return result

    @property
    def transform(self) -> str:
        """
        Return an SVG transform string for the point represented by this Coord.

        Returns:
            str: The SVG transform string.
        """
        return self.point.transform

    @staticmethod
    def middle(a: 'Coord', b: 'Coord') -> 'Coord':
        """
        Return the midpoint between two Coord objects.

        Args:
            a (Coord): The first Coord.
            b (Coord): The second Coord.

        Returns:
            Coord: The midpoint between the two coordinates.
        """
        return Coord(
            (a.row + b.row) / 2,
            (a.column + b.column) / 2
        )

    @property
    def point(self) -> Point:
        """
        Convert the Coord into a Point, scaling the row and column by 100.

        Returns:
            Point: The corresponding Point object.
        """
        return Point(self.column * 100, self.row * 100)

    @property
    def top_left(self) -> 'Coord':
        """
        Return the top-left corner of the cell that this Coord represents.

        Returns:
            Coord: The top-left corner coordinate.
        """
        return Coord(int(self.row), int(self.column))

    @property
    def center(self) -> 'Coord':
        """
        Return the center point of the cell that this Coord represents.

        Returns:
            Coord: The center coordinate.
        """
        return self.top_left + Coord(0.5, 0.5)

    @property
    def bottom_right(self) -> 'Coord':
        """
        Return the bottom-right corner of the cell that this Coord represents.

        Returns:
            Coord: The bottom-right corner coordinate.
        """
        return self.top_left + Coord(1, 1)

    @property
    def bottom_left(self) -> 'Coord':
        """
        Return the bottom-left corner of the cell that this Coord represents.

        Returns:
            Coord: The bottom-left corner coordinate.
        """
        return self.top_left + Coord(1, 0)

    @property
    def top_right(self) -> 'Coord':
        """
        Return the top-right corner of the cell that this Coord represents.

        Returns:
            Coord: The top-right corner coordinate.
        """
        return self.top_left + Coord(0, 1)

    @staticmethod
    def create_from_int(row_column: int) -> 'Coord':
        """
        Create a Coord object from an integer representing row and column values.

        Args:
            row_column (int): The integer to convert.

        Returns:
            Coord: The corresponding Coord object.
        """
        r, c = divmod(row_column, 10)
        return Coord(r, c)
