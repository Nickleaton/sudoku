"""List of Vectors."""
from typing import List, Optional, Iterator

from src.utils.coord import Coord
from src.utils.coord_list import CoordList
from src.utils.sudoku_exception import SudokuException
from src.utils.vector import Vector


class VectorListException(SudokuException):
    """Exception when handling VectorList."""


class VectorList:
    """List of Vectors."""

    def __init__(self, items: List[Vector]):
        self.items = items

    def __iter__(self) -> Iterator[Vector]:
        """Return an iterator for the vector list."""
        return iter(self.items)

    def __next__(self) -> Vector:
        """Get the next vector in the iteration."""
        return next(iter(self.items))

    def __contains__(self, other: Vector) -> bool:
        """Check if a vector is in the list."""
        return any(item == other for item in self.items)

    def __len__(self) -> int:
        """Return the number of vectors in the list."""
        return len(self.items)

    def __repr__(self) -> str:
        """Return a string representation of the vector list."""
        return f"{self.__class__.__name__}([{', '.join(repr(v) for v in self.items)}])"

    def __eq__(self, other: object) -> bool:
        """Check equality with another VectorList."""
        if not isinstance(other, VectorList):
            raise VectorListException(f"Cannot compare {type(other).__name__} with {self.__class__.__name__}")
        return self.items == other.items

    def __add__(self, other: object) -> 'VectorList':
        """Merge two vector lists."""
        if not isinstance(other, VectorList):
            raise VectorListException(f"Cannot merge with {type(other).__name__}")
        return VectorList(self.items + other.items)

    def sort(self) -> None:
        """Sort the vectors in the list."""
        self.items.sort()

    def merge_vectors(self) -> 'VectorList':
        """
        Merge vectors that are parallel and share endpoints.

        This helps because we can draw vectors, then have this
        algorithm optimize them.

        Returns:
            VectorList: A new list of merged vectors.
        """
        merged_items: List[Vector] = []

        for vector in self.items:
            merged = False  # Track if a merge occurred
            for i, merged_vector in enumerate(merged_items):
                if vector.mergeable(merged_vector):
                    merged_items[i] = vector.merge(merged_vector)
                    merged = True
                    break
            if not merged:  # If no merge occurred, append v
                merged_items.append(vector)

        return VectorList(sorted(merged_items))

    def find(self, coord: Coord) -> Optional[Coord]:
        """Find a coordinate in the vector list."""
        for item in self.items:
            if item.start == coord:
                return item.end
            if item.end == coord:
                return item.start
        return None

    @property
    def coords(self) -> CoordList:
        """Return a list of all coordinates in the vector list."""
        coords = CoordList([])
        for item in self.items:
            coords.add(item.start)
            coords.add(item.end)
        coords.sort()
        return coords
