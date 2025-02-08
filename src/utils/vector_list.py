"""VectorList."""
from collections.abc import Iterator

from src.utils.coord_list import CoordList
from src.utils.vector import Vector


class VectorListError(Exception):
    """Exception raised for errors in VectorList operations."""


class VectorList:
    """Represents a collection of Vectors with various utility methods."""

    def __init__(self, vectors: list[Vector] | None = None):
        """Initialize the VectorList with a given list of Vectors or an empty list.

        Args:
            vectors (list[Vectors] | None): A list of vectors. Defaults to an empty list if None.
        """
        self.vectors: list[Vector] = [] if vectors is None else vectors

    def __iter__(self) -> Iterator[Vector]:
        """Return an iterator over the vectors.

        Returns:
            Iterator[Vector]: The next vector in the list.
        """
        return iter(self.vectors)

    def __getitem__(self, index: int) -> Vector:
        """Retrieve the vector at the specified index.

        Args:
            index (int): The index of the vector to retrieve.

        Returns:
            Vector: The vector at the specified index.
        """
        return self.vectors[index]

    def __contains__(self, vector) -> bool:
        """Check if a vector is in the VectorList.

        Args:
            vector (Vector): The vector to check for presence.

        Returns:
            bool: True if the vector is in the list, False otherwise.
        """
        return vector in self.vectors

    def __len__(self) -> int:
        """Return the number of vectors.

        Returns:
            int: The number of vectors in the VectorList.
        """
        return len(self.vectors)

    def __repr__(self) -> str:
        """Return a string representation of the VectorList.

        Returns:
            str: A string representation of the VectorList.
        """
        return f'{self.__class__.__name__}([{", ".join(map(repr, self.vectors))}])'

    def __eq__(self, other) -> bool:
        """Check equality with another VectorList.

        Args:
            other (object): The object to compare with.

        Raises:
            VectorListError: If the other object is not an instance of VectorList.

        Returns:
            bool: True if the two VectorLists are equal, False otherwise.
        """
        if not isinstance(other, VectorList):
            raise VectorListError(f'Cannot compare {type(other).__name__} with {self.__class__.__name__}')
        return self.vectors == other.vectors

    def extend(self, other) -> None:
        """Extend the VectorList with another VectorList.

        Args:
            other (VectorList): The VectorList to extend with.

        Raises:
            VectorListError: If the other object is not an instance of VectorList.
        """
        if not isinstance(other, VectorList):
            raise VectorListError(f'Cannot extend with {type(other).__name__}')
        self.vectors.extend(other.vectors)

    def __add__(self, other) -> 'VectorList':
        """Return a new VectorList combining both lists.

        Args:
            other (VectorList): The VectorList to add.

        Raises:
            VectorListError: If the other object is not an instance of VectorList.

        Returns:
            VectorList: A new VectorList containing vectors from both lists.
        """
        if not isinstance(other, VectorList):
            raise VectorListError(f'Cannot add {type(other).__name__}')
        return VectorList(self.vectors + other.vectors)

    def sort(self) -> None:
        """Sort the vectors in place.

        This method sorts the vectors in the VectorList according to their natural order.
        """
        self.vectors.sort()

    def merge_vectors(self) -> 'VectorList':
        """Merge parallel vectors that share endpoints.

        This method combines vectors that are parallel and share the same endpoints.

        Returns:
            VectorList: A new VectorList with merged vectors, sorted.
        """
        merged_vectors: list[Vector] = []
        for vector in self.vectors:
            for index, merged_vector in enumerate(merged_vectors):
                if vector.mergeable(merged_vector):
                    merged_vectors[index] = vector.merge(merged_vector)
                    break
            else:
                merged_vectors.append(vector)
        return VectorList(sorted(merged_vectors))

    @property
    def coords(self):
        """Return a CoordList of all unique coordinates in the VectorList.

        Returns:
            CoordList: A CoordList containing all unique coordinates from the vectors in the VectorList.
        """
        coords: CoordList = CoordList([])
        for vector in self.vectors:
            coords.add(vector.start)
            coords.add(vector.end)
        return coords
