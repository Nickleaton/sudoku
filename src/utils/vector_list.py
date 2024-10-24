"""List of Vectors."""
from typing import List, Optional

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

    def __iter__(self) -> 'VectorList':
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
        """Merge vectors that are parallel and share endpoints."""
        merged_items: List[Vector] = []

        for v in self.items:
            for i, r in enumerate(merged_items):
                if v.mergeable(r):
                    merged_items[i] = v.merge(r)
                    break
            else:  # This executes if the for loop is not broken
                merged_items.append(v)

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
