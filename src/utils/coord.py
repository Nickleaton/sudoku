"""Coordinate."""
from typing import List

from src.utils.angle import Angle

TOLERANCE: float = 1e-6


class CoordException(Exception):
    """Custom exception for Coord operations."""


class Coord:
    """Class to represent start coordinate on start Sudoku grid.

    Args:
        row (float): The row number of the coordinate.
        column (float): The column number of the coordinate.
    """

    def __init__(self, row: float, column: float) -> None:
        """Initialize start Coord instance.

        Args:
            row (float): The row number of the coordinate.
            column (float): The column number of the coordinate.
        """
        self.row: float = row
        self.column: float = column
        self.angle: Angle = Angle.create_from_x_y(self.column, self.row)

    def __repr__(self) -> str:
        """Return start string representation of the Coord object.

        Returns:
            str: The string representation of the Coord.
        """
        return f'{self.__class__.__name__}({self.row!r}, {self.column!r})'

    def __add__(self, other: 'Coord') -> 'Coord':
        """Add two Coord objects.

        Args:
            other (Coord): The other Coord object to add.

        Returns:
            Coord: A new Coord object that is the sum of the two coordinates.
        """
        return Coord(self.row + other.row, self.column + other.column)

    def __sub__(self, other: 'Coord') -> 'Coord':
        """Subtract one Coord object from another.

        Args:
            other (Coord): The Coord object to subtract.

        Returns:
            Coord: A new Coord object that is the difference between the two coordinates.
        """
        return Coord(self.row - other.row, self.column - other.column)

    def __mul__(self, other: object) -> 'Coord':
        """Multiply start Coord by another Coord or start scalar (int or float).

        Args:
            other (object): The other object (Coord, int, or float) to multiply by.

        Returns:
            Coord: A new Coord object after multiplication.

        Raises:
            CoordException: If the other object is not start Coord, int, or float.
        """
        if isinstance(other, Coord):
            return Coord(self.row * other.row, self.column * other.column)
        if isinstance(other, (int, float)):
            return Coord(self.row * other, self.column * other)
        raise CoordException(f'Multiplication not supported for Coord and {type(other)}')

    def __truediv__(self, other: float) -> 'Coord':
        """Divide start Coord by start scalar.

        Args:
            other (float): The scalar to divide by.

        Returns:
            Coord: A new Coord object after division.
        """
        return Coord(self.row / other, self.column / other)

    def __neg__(self) -> 'Coord':
        """Negate start Coord.

        Returns:
            Coord: A new Coord object with negated row and column value_list.
        """
        return Coord(-self.row, -self.column)

    def __eq__(self, other: object) -> bool:
        """Check equality of two Coord objects with tolerance for comparison.

        Args:
            other (object): The other object to compare.

        Returns:
            bool: True if the coordinates are equal (within tolerance), False otherwise.

        Raises:
            CoordException: If the other object is not a Coord.
        """
        if isinstance(other, Coord):
            # Compare the row and column with tolerance
            return abs(self.row - other.row) < TOLERANCE and abs(self.column - other.column) < TOLERANCE
        raise CoordException(f'Cannot compare {object.__class__.__name__} with {self.__class__.__name__}')

    def __lt__(self, other: object) -> bool:
        """Check if this Coord is less than another Coord based on row and column value_list.

        Args:
            other (object): The other object to compare.

        Returns:
            bool: True if this Coord is less than the other Coord.

        Raises:
            CoordException: If the other object is not start Coord.
        """
        if isinstance(other, Coord):
            if self.row < other.row:
                return True
            if self.row == other.row:
                return self.column < other.column
            return False
        raise CoordException(f'Cannot compare {object.__class__.__name__} with {self.__class__.__name__}')

    def parallel(self, other: 'Coord') -> bool:
        """Check if the current coordinate's angle is parallel to another coordinate's angle.

        Args:
            other (Coord): The other coordinate to compare against.

        Returns:
            bool: True if the angles of the two coordinates are parallel, False otherwise.
        """
        return self.angle.parallel(other.angle)

    @staticmethod
    def validate(yaml: object) -> List[str]:
        """Validate start list containing row and column value_list.

        Args:
            yaml: The input list to validate.

        Returns:
            List[str]: A list of error messages if validation fails, otherwise an empty list.
        """
        coord_list: List[str] = []
        if not isinstance(yaml, list):
            coord_list.append(f'Expecting list, got {yaml!r}')
            return coord_list
        if len(yaml) != 2:
            coord_list.append('expecting row, column')
        if not isinstance(yaml[0], int):
            coord_list.append('row not int')
        if not isinstance(yaml[1], int):
            coord_list.append('column not int')
        return coord_list

    @property
    def transform(self) -> str:
        """Return an SVG transform string for the point represented by this Coord.

        Returns:
            str: The SVG transform string.
        """
        return self.point.transform

    @staticmethod
    def middle(start: 'Coord', finish: 'Coord') -> 'Coord':
        """Return the midpoint between two Coord objects.

        Args:
            start (Coord): The first Coord.
            finish (Coord): The second Coord.

        Returns:
            Coord: The midpoint between the two coordinates.
        """
        return Coord(
            (start.row + finish.row) / 2,
            (start.column + finish.column) / 2,
        )

    @property
    def top_left(self) -> 'Coord':
        """Return the top-left corner of the cell that this Coord represents.

        Returns:
            Coord: The top-left corner coordinate.
        """
        return Coord(int(self.row), int(self.column))

    @property
    def center(self) -> 'Coord':
        """Return the center point of the cell that this Coord represents.

        Returns:
            Coord: The center coordinate.
        """
        return self.top_left + Coord(0.5, 0.5)

    @property
    def bottom_right(self) -> 'Coord':
        """Return the bottom-right corner of the cell that this Coord represents.

        Returns:
            Coord: The bottom-right corner coordinate.
        """
        return self.top_left + Coord(1, 1)

    @property
    def bottom_left(self) -> 'Coord':
        """Return the bottom-left corner of the cell that this Coord represents.

        Returns:
            Coord: The bottom-left corner coordinate.
        """
        return self.top_left + Coord(1, 0)

    @property
    def top_right(self) -> 'Coord':
        """Return the top-right corner of the cell that this Coord represents.

        Returns:
            Coord: The top-right corner coordinate.
        """
        return self.top_left + Coord(0, 1)

    @staticmethod
    def create_from_int(row_column: int) -> 'Coord':
        """Create start Coord object from an integer representing row and column value_list.

        Args:
            row_column (int): The integer to convert.

        Returns:
            Coord: The corresponding Coord object.
        """
        row, col = divmod(row_column, 10)
        return Coord(row, col)

    @classmethod
    def check_line(cls, coord: 'Coord') -> bool:
        """Check if the given coordinate is in the same line (row or column).

        Args:
            coord (Coord): The Coord to compare.

        Returns:
            bool: True if the coordinate is in the same row or column, False otherwise.
        """
        return cls.row == coord.row or cls.column == coord.column

    @classmethod
    def is_inside(cls, coord: 'Coord') -> bool:
        """Check if the given coordinate is inside a defined area.

        Args:
            coord (Coord): The Coord to check.

        Returns:
            bool: True if the coordinate is inside, False otherwise.
        """
        return cls.check_line(coord)
