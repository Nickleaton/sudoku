"""List of Vectors."""
from typing import List, Optional

from src.utils.coord import Coord
from src.utils.coord_list import CoordList
from src.utils.vector import Vector


class VectorListException(Exception):
    """Exception when handling VectorList."""


class VectorList:
    """List of Vectors."""

    def __init__(self, items: List[Vector]):
        self.items = items
        self.n = 0

    def __iter__(self) -> 'VectorList':
        self.n = 0
        return self

    def __next__(self) -> Vector:
        if self.n < len(self):
            result = self.items[self.n]
            self.n += 1
        else:
            raise StopIteration
        return result

    def __contains__(self, other: Vector) -> bool:
        for item in self:
            if item == other:
                return True
        return False

    def __len__(self) -> int:
        return len(self.items)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}([{', '.join([repr(v) for v in self.items])}])"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, VectorList):
            if len(self.items) != len(other.items):
                return False
            for i, o in zip(self.items, other.items):
                if i != o:
                    return False
            return True
        raise VectorListException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __add__(self, other: object) -> 'VectorList':
        """
        Merge two vector lists.

        :param other: VectorList
        :return: merged VectorList
        """
        if isinstance(other, VectorList):
            result = VectorList([])
            result.items.extend(self.items)
            result.items.extend(other.items)
            return result
        raise VectorListException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def sort(self) -> None:
        """Sort the items on the basis of vector comparison."""
        self.items = sorted(self.items)

    def merge_vectors(self) -> 'VectorList':
        """
        Merge vectors.

        If a vector is parallel to another vector in the list, and shares an end point or a start point,
        it is mergeable.

        :return: Vector list
        """
        items: List[Vector] = []
        for v in self.items:
            merged = False
            for i, r in enumerate(items):
                if v.mergeable(r):
                    items[i] = v.merge(r)
                    merged = True
            if not merged:
                items.append(v)

        return VectorList(sorted(items))

    def find(self, coord: Coord) -> Optional[Coord]:
        """
        Find coord in VectorList.

        Find the end coord of a vector if the start is 'coord'.
        Find the start coord of a vector if the end is 'coord'.

        :param coord:
        :return: coord
        """
        for item in self.items:
            if item.start == coord:
                return item.end
            if item.end == coord:
                return item.start
        return None

    @property
    def coords(self) -> CoordList:
        """
        Return a list of all coordinates in the list of vectors.

        :return: CoordList
        """
        coords = CoordList([])
        for item in self.items:
            coords.add(item.start)
            coords.add(item.end)
        coords.sort()
        return coords
