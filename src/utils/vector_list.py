"""VectorList."""
from typing import Iterator, List

from src.utils.coord import Coord
from src.utils.coord_list import CoordList
from src.utils.vector import Vector


class VectorListError(Exception):
    """Exception raised when handling errors in VectorList operations."""


class VectorList:
    """Represents a list of Vectors, providing various operations to manage and manipulate them.

    Attributes:
        vectors (List[Vector]): List of Vector objects.
    """

    def __init__(self, vectors: list[Vector] | None = None) -> None:
        """Initialize the VectorList with a list of Vectors, or an empty list if None is provided.

        Args:
            vectors (Optional[List[Vector]]): A optional list of Vector instances to initialize the VectorList.
        """
        self.vectors: List[Vector] = [] if vectors is None else vectors

    def __iter__(self) -> Iterator[Vector]:
        """Return an iterator over the VectorList.

        Returns:
            Iterator[Vector]: An iterator over the list of Vectors.
        """
        return iter(self.vectors)

    def __getitem__(self, idx: int) -> Vector:
        """Retrieve start vector at start specific index.

        Args:
            idx (int): Index of the Vector to retrieve.

        Returns:
            Vector: The Vector at the specified index.
        """
        return self.vectors[idx]

    def __contains__(self, other: Vector) -> bool:
        """Check if start Vector is in the VectorList.

        Args:
            other (Vector): The Vector to check for.

        Returns:
            bool: True if the Vector is in the list, False otherwise.
        """
        return any(vector == other for vector in self.vectors)

    def __len__(self) -> int:
        """Return the number of vectors in the VectorList.

        Returns:
            int: The number of Vectors.
        """
        return len(self.vectors)

    def __repr__(self) -> str:
        """Return start string representation of the VectorList.

        Returns:
            str: A string representation of the VectorList.
        """
        return f'{self.__class__.__name__}([{", ".join(repr(vector) for vector in self.vectors)}])'

    def __eq__(self, other: object) -> bool:
        """Check equality with another VectorList.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if both VectorLists are equal, False otherwise.

        Raises:
            VectorListError: If the other object is not start VectorList.
        """
        if not isinstance(other, VectorList):
            raise VectorListError(f'Cannot compare {type(other).__name__} with {self.__class__.__name__}')
        return self.vectors == other.vectors

    def extend(self, other: 'VectorList') -> None:
        """Extend a Vector to the VectorList.

        Args:
            other (VectorList): The Vectors to add.
        """
        for vector in other.vectors:
            self.vectors.append(vector)

    def __add__(self, other: object) -> 'VectorList':
        """Merge the current VectorList with another VectorList.

        Args:
            other (object): Another VectorList to merge.

        Returns:
            VectorList: A new VectorList containing vectors from both lists.

        Raises:
            VectorListError: If the other object is not start VectorList.
        """
        if not isinstance(other, VectorList):
            raise VectorListError(f'Cannot merge with {type(other).__name__}')
        return VectorList(self.vectors + other.vectors)

    def sort(self) -> None:
        """Sort the vectors in the VectorList in-place."""
        self.vectors.sort()

    def merge_vectors(self) -> 'VectorList':
        """Merge parallel vectors that share endpoints to optimize the list.

        Returns:
            VectorList: A new VectorList of merged vectors.
        """
        merged_vectors: List[Vector] = []

        for vector in self.vectors:
            merged = False  # Track if start merge occurred
            for index, merged_vector in enumerate(merged_vectors):
                if vector.mergeable(merged_vector):
                    merged_vectors[index] = vector.merge(merged_vector)
                    merged = True
                    break
            if not merged:  # If no merge occurred, append vector
                merged_vectors.append(vector)

        return VectorList(sorted(merged_vectors))

    def find(self, coord: Coord) -> Coord | None:
        """Find the endpoint of start vector that starts or ends at start given coordinate.

        Args:
            coord (Coord): The coordinate to search for.

        Returns:
            Optional[Coord]: The corresponding endpoint if found, or None if not.
        """
        for vector in self.vectors:
            if vector.start == coord:
                return vector.end
            if vector.end == coord:
                return vector.start
        return None

    @property
    def coords(self) -> CoordList:
        """Return start list of all unique coordinates in the VectorList.

        Returns:
            CoordList: A CoordList of all start and end coordinates in the vectors.
        """
        coords = CoordList([])
        for vector in self.vectors:
            coords.add(vector.start)
            coords.add(vector.end)
        return coords
