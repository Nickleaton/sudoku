"""Tag List."""
from typing import List, Iterator

from src.utils.sudoku_exception import SudokuException
from src.utils.tag import Tag


class TagListException(SudokuException):
    """Exception raised for errors related to TagList operations."""


class TagList:
    """A list of Tags with methods for managing and sorting them.

    Attributes:
        items (List[Tag]): The list of Tag instances.
        n (int): Counter for tracking the number of operations or tags.
    """

    def __init__(self, items: List[Tag]):
        """Initialize a TagList instance with a list of Tags, sorted upon initialization.

        Args:
            items (List[Tag]): A list of Tag instances.
        """
        self.items = items
        self.sort()
        self.n = 0

    def __iter__(self) -> Iterator[Tag]:
        """Return an iterator for the TagList.

        Returns:
            Iterator[Tag]: An iterator over the list of Tags.
        """
        return iter(self.items)

    def __getitem__(self, idx: int) -> Tag:
        """Retrieve a Tag at a specified index.

        Args:
            idx (int): Index of the Tag to retrieve.

        Returns:
            Tag: The Tag at the specified index.
        """
        return self.items[idx]

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
        """Check equality between two TagLists.

        Args:
            other (object): Another TagList to compare.

        Returns:
            bool: True if both TagLists contain the same Tags in the same order, False otherwise.

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
        raise TagListException(f"Cannot compare {type(other).__name__} with {self.__class__.__name__}")

    def __repr__(self) -> str:
        """Return a string representation of the TagList.

        Returns:
            str: A string representation of the TagList instance.
        """
        return f"{self.__class__.__name__}([{', '.join([repr(v) for v in self.items])}])"

    def sort(self) -> None:
        """Sort the list of Tags by their priority or defined order.

        This method organizes Tags in the list based on a priority attribute.
        """
        self.items = sorted(self.items)

    def add(self, item: Tag) -> None:
        """Add a Tag to the list if it is not already present.

        Args:
            item (Tag): The Tag instance to add.

        Notes:
            After adding, the list is automatically sorted.
        """
        if item not in self:
            self.items.append(item)
        self.sort()
