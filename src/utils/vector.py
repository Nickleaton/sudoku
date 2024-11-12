"""Vector."""
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.sudoku_exception import SudokuException


class VectorException(SudokuException):
    """Exception raised for errors related to Vector operations."""


class Vector:
    """Represents a vector defined by a start and end coordinate."""

    def __init__(self, start: Coord, end: Coord):
        """Construct a vector from start and end coordinates.

        Args:
            start (Coord): The starting coordinate of the vector.
            end (Coord): The ending coordinate of the vector.
        """
        self.start: Coord = start
        self.end: Coord = end

    def __eq__(self, other: object) -> bool:
        """Check if two vectors are equal based on their start and end coordinates.

        Args:
            other (object): The other vector to compare.

        Returns:
            bool: True if both vectors are equal, False otherwise.

        Raises:
            VectorException: If the other object is not a Vector.
        """
        if not isinstance(other, Vector):
            raise VectorException(f"Cannot compare with non-Vector type: {type(other).__name__}")
        return (self.start == other.start and self.end == other.end) or \
            (self.start == other.end and self.end == other.start)

    def __lt__(self, other: 'Vector') -> bool:
        """Compare two vectors based on their starting and ending coordinates.

        Args:
            other (Vector): The other vector to compare.

        Returns:
            bool: True if this vector is less than the other vector.
        """
        if not isinstance(other, Vector):
            raise VectorException(f"Cannot compare with non-Vector type: {type(other).__name__}")
        return (self.start < other.start) or \
            (self.start == other.start and self.end < other.end)

    def __le__(self, other: 'Vector') -> bool:
        """Compare two vectors based on their starting and ending coordinates.

        Args:
            other (Vector): The other vector to compare.

        Returns:
            bool: True if this vector is less than or equal the other vector.
        """
        if self == other:
            return True
        return self < other

    def __neg__(self) -> 'Vector':
        """Return the negation of the vector.

        Returns:
            Vector: A new vector with the start and end swapped.
        """
        return Vector(self.end, self.start)

    def __add__(self, other: object) -> 'Vector':
        """Add a coordinate or another vector to this vector.

        Args:
            other (object): The object to add, can be a Coord or another Vector.

        Returns:
            Vector: A new vector resulting from the addition.

        Raises:
            VectorException: If addition is not supported with the given object.
        """
        if isinstance(other, Coord):
            return Vector(self.start + other, self.end + other)
        if isinstance(other, Vector):
            return Vector(self.start + other.start, self.end + other.end)
        raise VectorException(f'Addition  not supported for Vector and {other.__class__.__name__}')

    @property
    def direction(self) -> Direction:  # pylint: disable=too-many-return-statements
        """Determine the direction of the vector.

        Returns:
            Direction: The direction of the vector (UP, DOWN, LEFT, RIGHT, CENTER).
        """
        # Only for orthogonal
        if self.start.row == self.end.row:  # Horizontal
            return Direction.LEFT if self.start.column < self.end.column else \
                Direction.RIGHT if self.start.column > self.end.column else \
                    Direction.CENTER
        if self.start.column == self.end.column:  # Vertical
            return Direction.UP if self.start.row < self.end.row else \
                Direction.DOWN if self.start.row > self.end.row else \
                    Direction.CENTER
        return Direction.CENTER # pragma: no cover

    def mergeable(self, other: 'Vector') -> bool:
        """Check if this vector can be merged with another vector.

        Args:
            other (Vector): The other vector to check.

        Returns:
            bool: True if the vectors are mergeable, False otherwise.
        """
        # Check all combinations of start and ends and if connected
        connected: bool = (
                self.start == other.start or
                self.start == other.end or
                self.end == other.start or
                self.end == other.end
        )
        return connected and self.direction.parallel(other.direction)

    def merge(self, other: 'Vector') -> 'Vector':
        """Merge this vector with another vector if they are mergeable.

        Args:
            other (Vector): The other vector to merge.

        Returns:
            Vector: A new merged vector.

        Raises:
            VectorException: If the vectors are not mergeable.
        """
        if not self.mergeable(other):
            raise VectorException("Vectors are not mergeable")
        if self == other:
            return self
        if self.start == other.start:
            return Vector(self.end, other.end)
        if self.start == other.end:
            return Vector(self.end, other.start)
        if self.end == other.start:
            return Vector(self.start, other.end)
        # self.end == other.end
        return Vector(self.start, other.start)

    def __repr__(self) -> str:
        """Return a string representation of the vector.

        Returns:
            str: The representation of the vector including its start and end coordinates.
        """
        return f"{self.__class__.__name__}({repr(self.start)}, {repr(self.end)})"
