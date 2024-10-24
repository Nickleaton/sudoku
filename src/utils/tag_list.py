"""Tag List"""
from typing import List

from src.utils.sudoku_exception import SudokuException
from src.utils.tag import Tag


class TagListException(SudokuException):
    """Exception raised for errors related to TagList operations."""
    pass


class TagList:
    """List of Tags.

    Attributes:
        items (List[Tag]): The list of tags.
    """

    def __init__(self, items: List[Tag]):
        """Construct a TagList instance.

        Args:
            items (List[Tag]): A list of Tag instances.
        """
        self.items = items
        self.sort()
        self.n = 0

    def __iter__(self) -> 'TagList':
        """Return the iterator object for the TagList.

        Returns:
            TagList: The TagList instance itself.
        """
        self.n = 0
        return self

    def __next__(self) -> Tag:
        """Return the next Tag in the iteration.

        Returns:
            Tag: The next Tag instance.

        Raises:
            StopIteration: If there are no more Tags to return.
        """
        if self.n < len(self):
            result = self.items[self.n]
            self.n += 1
        else:
            raise StopIteration
        return result

    def __contains__(self, other: Tag) -> bool:
        """Check if a Tag is in the TagList.

        Args:
            other (Tag): The Tag instance to check.

        Returns:
            bool: True if the Tag is in the list, False otherwise.
        """
        for item in self.items:
            if item == other:
                return True
        return False

    def __len__(self) -> int:
        """Return the number of Tags in the TagList.

        Returns:
            int: The number of Tags in the list.
        """
        return len(self.items)

    def __eq__(self, other: object) -> bool:
        """Check if two TagLists are equal.

        Args:
            other (object): The other TagList to compare.

        Returns:
            bool: True if the TagLists have the same Tags in the same order, False otherwise.

        Raises:
            TagListException: If the other object is not a TagList.
        """
        if isinstance(other, TagList):
            if len(self.items) != len(other.items):
                return False
            for i, o in zip(self.items, other.items):
                if i != o:
                    return False
            return True
        raise TagListException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __repr__(self) -> str:
        """Return a string representation of the TagList.

        Returns:
            str: A string representation of the TagList instance.
        """
        return f"{self.__class__.__name__}([{', '.join([repr(v) for v in self.items])}])"

    def sort(self) -> None:
        """Sort the list of Tags by their priority.

        This method sorts the Tags in the list based on their defined order.
        """
        self.items = sorted(self.items)

    def add(self, item: Tag) -> None:
        """Add a Tag to the list if it is not already present.

        Args:
            item (Tag): The Tag instance to add.
        """
        if item not in self:
            self.items.append(item)
        self.sort()
