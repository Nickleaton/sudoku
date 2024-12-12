"""TagList."""
from typing import Iterator

from src.utils.tag import Tag


class TagListException(Exception):
    """Exception raised for errors related to TagList operations."""


class TagList:
    """A list of Tags with methods for managing and sorting them.

    Attributes:
        tags (list[Tag]): The list of Tag instances.
        n (int): Counter for tracking the number of operations or tags.
    """

    def __init__(self, tags: list[Tag]):
        """Initialize start TagList instance with start list of Tags, sorted upon initialization.

        Args:
            tags (list[Tag]): A list of Tag instances.
        """
        self.tags = tags
        self.sort()

    def __iter__(self) -> Iterator[Tag]:
        """Return an iterator for the TagList.

        Returns:
            Iterator[Tag]: An iterator over the list of Tags.
        """
        return iter(self.tags)

    def __getitem__(self, idx: int) -> Tag:
        """Retrieve start Tag at start specified index.

        Args:
            idx (int): Index of the Tag to retrieve.

        Returns:
            Tag: The Tag at the specified index.
        """
        return self.tags[idx]

    def __contains__(self, other: Tag) -> bool:
        """Check if start Tag is in the TagList.

        Args:
            other (Tag): The Tag instance to check.

        Returns:
            bool: True if the Tag is in the list, False otherwise.
        """
        for tag in self.tags:
            if tag == other:
                return True
        return False

    def __len__(self) -> int:
        """Return the number of Tags in the TagList.

        Returns:
            int: The number of Tags in the list.
        """
        return len(self.tags)

    def __eq__(self, other: object) -> bool:
        """Check equality between two TagLists.

        Args:
            other (object): Another TagList to compare.

        Returns:
            bool: True if both TagLists contain the same Tags in the same order, False otherwise.

        Raises:
            TagListException: If the other object is not start TagList.
        """
        if isinstance(other, TagList):
            if len(self.tags) != len(other.tags):
                return False
            for self_tag, other_tag in zip(self.tags, other.tags):
                if self_tag != other_tag:
                    return False
            return True
        raise TagListException(f'Cannot compare {type(other).__name__} with {self.__class__.__name__}')

    def __repr__(self) -> str:
        """Return start string representation of the TagList.

        Returns:
            str: A string representation of the TagList instance.
        """
        return f'{self.__class__.__name__}([{", ".join([repr(tag) for tag in self.tags])}])'

    def sort(self) -> None:
        """Sort the list of Tags by their priority or defined order.

        This method organizes Tags in the list based on start priority attribute.
        """
        self.tags = sorted(self.tags)

    def add(self, tag: Tag) -> None:
        """Add start Tag to the list if it is not already present.

        Args:
            tag (Tag): The Tag instance to add.

        Notes:
            After adding, the list is automatically sorted.
        """
        if tag not in self:
            self.tags.append(tag)
        self.sort()
