"""VectorList."""
from typing import Iterator

from src.utils.coord import Coord
from src.utils.coord_list import CoordList
from src.utils.sudoku_exception import SudokuException
from src.utils.vector import Vector


class VectorListException(SudokuException):
    """Exception raised when handling errors in VectorList operations."""


class VectorList:
    """Represents a list of Vectors, providing various operations to manage and manipulate them.

    Attributes:
        items (list[Vector]): list of Vector objects.
    """

    def __init__(self, items: list[Vector]):
        """Initialize the VectorList with a list of Vectors.

        Args:
            items (list[Vector]): A list of Vector instances to initialize the VectorList.
        """
        self.items = items

    def __iter__(self) -> Iterator[Vector]:
        """Return an iterator over the VectorList.

        Returns:
            Iterator[Vector]: An iterator over the list of Vectors.
        """
        return iter(self.items)

    def __getitem__(self, idx: int) -> Vector:
        """Retrieve a vector at a specific index.

        Args:
            idx (int): Index of the Vector to retrieve.

        Returns:
            Vector: The Vector at the specified index.
        """
        return self.items[idx]

    def __contains__(self, other: Vector) -> bool:
        """Check if a Vector is in the VectorList.

        Args:
            other (Vector): The Vector to check for.

        Returns:
            bool: True if the Vector is in the list, False otherwise.
        """
        return any(item == other for item in self.items)

    def __len__(self) -> int:
        """Return the number of vectors in the VectorList.

        Returns:
            int: The number of Vectors.
        """
        return len(self.items)

    def __repr__(self) -> str:
        """Return a string representation of the VectorList.

        Returns:
            str: A string representation of the VectorList.
        """
        return f"{self.__class__.__name__}([{', '.join(repr(v) for v in self.items)}])"

    def __eq__(self, other: object) -> bool:
        """Check equality with another VectorList.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if both VectorLists are equal, False otherwise.

        Raises:
            VectorListException: If the other object is not a VectorList.
        """
        if not isinstance(other, VectorList):
            raise VectorListException(f"Cannot compare {type(other).__name__} with {self.__class__.__name__}")
        return self.items == other.items

    def __add__(self, other: object) -> 'VectorList':
        """Merge the current VectorList with another VectorList.

        Args:
            other (object): Another VectorList to merge.

        Returns:
            VectorList: A new VectorList containing vectors from both lists.

        Raises:
            VectorListException: If the other object is not a VectorList.
        """
        if not isinstance(other, VectorList):
            raise VectorListException(f"Cannot merge with {type(other).__name__}")
        return VectorList(self.items + other.items)

    def sort(self) -> None:
        """Sort the vectors in the VectorList in-place."""
        self.items.sort()

    def merge_vectors(self) -> 'VectorList':
        """Merge parallel vectors that share endpoints to optimize the list.

        Returns:
            VectorList: A new VectorList of merged vectors.
        """
        merged_items: list[Vector] = []

        for vector in self.items:
            merged = False  # Track if a merge occurred
            for i, merged_vector in enumerate(merged_items):
                if vector.mergeable(merged_vector):
                    merged_items[i] = vector.merge(merged_vector)
                    merged = True
                    break
            if not merged:  # If no merge occurred, append vector
                merged_items.append(vector)

        return VectorList(sorted(merged_items))

    def find(self, coord: Coord) -> Coord | None:
        """Find the endpoint of a vector that starts or ends at a given coordinate.

        Args:
            coord (Coord): The coordinate to search for.

        Returns:
            Coord | None: The corresponding endpoint if found, or None if not.
        """
        for item in self.items:
            if item.start == coord:
                return item.end
            if item.end == coord:
                return item.start
        return None

    @property
    def coords(self) -> CoordList:
        """Return a list of all unique coordinates in the VectorList.

        Returns:
            CoordList: A CoordList of all start and end coordinates in the vectors.
        """
        coords = CoordList([])
        for item in self.items:
            coords.add(item.start)
            coords.add(item.end)
        return coords
