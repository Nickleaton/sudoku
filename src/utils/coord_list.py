from typing import List
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
        self.items = items
        self.sort()
        self.n = 0

    def __iter__(self) -> 'CoordList':
        """
        Initializes the iterator for the CoordList.

        Returns:
            CoordList: The current instance as an iterable.
        """
        self.n = 0
        return self

    def __next__(self) -> Coord:
        """
        Retrieves the next item in the CoordList during iteration.

        Returns:
            Coord: The next Coord in the list.

        Raises:
            StopIteration: When the iteration is complete.
        """
        if self.n < len(self):
            result = self.items[self.n]
            self.n += 1
        else:
            raise StopIteration
        return result

    def __contains__(self, other: Coord) -> bool:
        """
        Checks if a given Coord is in the list.

        Args:
            other (Coord): The Coord object to check.

        Returns:
            bool: True if the Coord is in the list, otherwise False.
        """
        for item in self.items:
            if item == other:
                return True
        return False

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
        if isinstance(other, CoordList):
            if len(self.items) != len(other.items):
                return False
            for i, o in zip(self.items, other.items):
                if i != o:
                    return False
            return True
        raise CoordListException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __repr__(self) -> str:
        """
        Returns a string representation of the CoordList.

        Returns:
            str: The string representation of the CoordList.
        """
        return f"{self.__class__.__name__}([{', '.join([repr(v) for v in self.items])}])"

    def sort(self) -> None:
        """
        Sorts the Coord objects in the list.
        """
        self.items = sorted(self.items)

    def add(self, item: Coord) -> None:
        """
        Adds a Coord to the list if it's not already present, and sorts the list.

        Args:
            item (Coord): The Coord object to add.
        """
        if item not in self:
            self.items.append(item)
        self.sort()
