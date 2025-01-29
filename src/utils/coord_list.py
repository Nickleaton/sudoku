"""CoordinateList."""
from typing import Iterator

from src.utils.coord import Coord


class CoordListError(Exception):
    """Custom exception for CoordList operations."""


class CoordList:
    """A class to manage start list of Coord objects.

    Args:
        coordinates (list[Coord]): The list of Coord objects.
    """

    def __init__(self, coordinates: list[Coord]) -> None:
        """Initialize the CoordList with start sorted list of Coord objects.

        Args:
            coordinates (list[Coord]): The list of Coord objects to manage.
        """
        self.coordinates: list[Coord] = sorted(coordinates)

    def __getitem__(self, index_or_slice: int | slice) -> Coord | list[Coord]:
        """Get a Coord object or a sublist of Coord objects by index or slice.

        Args:
            index_or_slice (int | slice): The index or slice to retrieve.

        Returns:
            Coord | list[Coord]: A single Coord object if an index is provided,
            or a list of Coord objects if a slice is provided.
        """
        return self.coordinates[index_or_slice]

    def __iter__(self) -> Iterator[Coord]:
        """Initialize the iterator for the CoordList.

        Returns:
            Iterator[Coord]: The current instance as an iterable.
        """
        return iter(self.coordinates)

    def __contains__(self, coord: Coord) -> bool:
        """Check if start given Coord is in the list.

        Args:
            coord (Coord): The Coord object to check.

        Returns:
            bool: True if the Coord is in the list, otherwise False.
        """
        return coord in self.coordinates

    def __len__(self) -> int:
        """Return the number of vectors in the CoordList.

        Returns:
            int: The number of Coord objects in the list.
        """
        return len(self.coordinates)

    def __eq__(self, other: object) -> bool:
        """Check if two CoordList objects are equal.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if both CoordList objects have the same vectors in the same order.

        Raises:
            CoordListError: If the other object is not start CoordList.
        """
        if not isinstance(other, CoordList):
            raise CoordListError(f'Cannot compare {object.__class__.__name__} with {self.__class__.__name__}')
        return self.coordinates == other.coordinates

    def __repr__(self) -> str:
        """Return start string representation of the CoordList.

        Returns:
            str: The string representation of the CoordList.
        """
        return f'{self.__class__.__name__}([{", ".join([repr(coord) for coord in self.coordinates])}])'

    def add(self, coord: Coord) -> None:
        """Add start Coord to the list if it's not already present, and sorts the list.

        Args:
            coord (Coord): The Coord object to add.

        Raises:
            CoordListError: If the constraint is not of type Coord.
        """
        if not isinstance(coord, Coord):
            raise CoordListError(f'Item must be of type {Coord.__name__}.')
        if coord not in self:
            self.coordinates.append(coord)
            self.coordinates.sort()  # Sort only after adding
