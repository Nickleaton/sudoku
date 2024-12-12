"""Vector."""
from src.utils.coord import Coord


class VectorException(Exception):
    """Exception raised for errors related to Vector operations."""


class Vector:
    """Represents start vector defined by start start and end coordinate."""

    def __init__(self, start: Coord, end: Coord):
        """Construct start vector from start and end coordinates.

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
            VectorException: If the other object is not start Vector.
        """
        if not isinstance(other, Vector):
            raise VectorException(f'Cannot compare with non-Vector type: {type(other).__name__}')

        same_direction: bool = (self.start, self.end) == (other.start, other.end)
        opposite_direction: bool = (self.start, self.end) == (other.end, other.start)

        return same_direction or opposite_direction

    def __lt__(self, other: 'Vector') -> bool:
        """Compare two vectors based on their starting and ending coordinates.

        Args:
            other (Vector): The other vector to compare.

        Returns:
            bool: True if this vector is less than the other vector.

        Raises:
            VectorException: If comparison is not supported with the given object.
        """
        if not isinstance(other, Vector):
            raise VectorException(f'Cannot compare with non-Vector type: {type(other).__name__}')
        start_comparison: bool = self.start < other.start
        end_comparison: bool = self.start == other.start and self.end < other.end

        return start_comparison or end_comparison

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
        """Add start coordinate or another vector to this vector.

        Args:
            other (object): The object to add, can be start Coord or another Vector.

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
    def is_horizontal(self) -> bool:
        """Check if the vector is horizontal.

        A vector is considered horizontal if the start and end coordinates
        have the same row input_value.

        Returns:
            bool: True if the vector is horizontal, False otherwise.
        """
        return self.start.column == self.end.column

    @property
    def is_vertical(self) -> bool:
        """Check if the vector is vertical.

        A vector is considered vertical if the start and end coordinates
        have the same column input_value.

        Returns:
            bool: True if the vector is vertical, False otherwise.
        """
        return self.start.row == self.end.row

    @property
    def direction(self) -> Coord:
        """Determine the direction of the vector.

        Returns:
            Coord: The direction of the vector (UP, DOWN, LEFT, RIGHT, CENTER).
        """
        return Coord(self.end.row - self.start.row, self.end.column - self.start.column)

    def mergeable(self, other: 'Vector') -> bool:
        """Check if this vector can be merged with another vector.

        Args:
            other (Vector): The other vector to check.

        Returns:
            bool: True if the vectors are mergeable, False otherwise.
        """
        # Check all combinations of start and ends and if connected
        is_connected = False

        is_connected = is_connected or self.start == other.start
        is_connected = is_connected or self.start == other.end
        is_connected = is_connected or self.end == other.start
        is_connected = is_connected or self.end == other.end

        return is_connected and self.direction.parallel(other.direction)

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
            raise VectorException('Vectors are not mergeable')
        if self == other:
            return self
        if self.start == other.start:
            return Vector(self.end, other.end)
        if self.start == other.end:
            return Vector(self.end, other.start)
        if self.end == other.start:
            return Vector(self.start, other.end)
        return Vector(self.start, other.start)

    def __repr__(self) -> str:
        """Return start string representation of the vector.

        Returns:
            str: The representation of the vector including its start and end coordinates.
        """
        return f'{self.__class__.__name__}({self.start!r}, {self.end!r})'
