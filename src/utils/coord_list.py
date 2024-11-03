from typing import List, Iterator

from src.items.item import SudokuException
from src.utils.coord import Coord


class CoordListException(SudokuException):
    """
    Custom exception for CoordList operations.
    """
    pass


class CoordList:
    """
    A class to manage a list of Coord objects.

    Args:
        items (List[Coord]): The list of Coord objects.
    """

    def __init__(self, items: List[Coord]):
        self.items = sorted(items)

    def __iter__(self) -> Iterator[Coord]:
        """
        Initializes the iterator for the CoordList.

        Returns:
            CoordList: The current instance as an iterable.
        """
        return iter(self.items)

    def __contains__(self, other: Coord) -> bool:
        """
        Checks if a given Coord is in the list.

        Args:
            other (Coord): The Coord object to check.

        Returns:
            bool: True if the Coord is in the list, otherwise False.
        """
        return other in self.items

    def __len__(self) -> int:
        """
        Returns the number of items in the CoordList.

        Returns:
            int: The number of Coord objects in the list.
        """
        return len(self.items)

    def __eq__(self, other: object) -> bool:
        """
        Checks if two CoordList objects are equal.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if both CoordList objects have the same items in the same order.

        Raises:
            CoordListException: If the other object is not a CoordList.
        """
        if not isinstance(other, CoordList):
            raise CoordListException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")
        return self.items == other.items

    def __repr__(self) -> str:
        """
        Returns a string representation of the CoordList.

        Returns:
            str: The string representation of the CoordList.
        """
        return f"{self.__class__.__name__}([{', '.join([repr(v) for v in self.items])}])"

    def add(self, item: Coord) -> None:
        """
        Adds a Coord to the list if it's not already present, and sorts the list.

        Args:
            item (Coord): The Coord object to add.
        """
        if not isinstance(item, Coord):
            raise CoordListException(f"Item must be of type {Coord.__name__}.")
        if item not in self:
            self.items.append(item)
            self.items.sort()  # Sort only after adding
