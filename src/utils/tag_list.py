"""TagList."""
from bisect import bisect_left
from collections.abc import Iterator

from src.utils.tag import Tag


class TagListError(Exception):
    """Exception raised for errors related to TagList operations."""


class TagList:
    """A list of Tags with methods for managing and sorting them."""

    def __init__(self, tags: list[Tag] | None = None):
        """Initialize a TagList with an optional list of Tags.

        Args:
            tags (list[Tag], optional): A list of Tags to for the TagList. Defaults to an empty list if None.
        """
        self.tags = list(tags) if tags else []
        self.sort()

    def __iter__(self) -> Iterator[Tag]:
        """Return an iterator for the TagList.

        Returns:
            Iterator[Tag]: Iterator over the Tags in the TagList.
        """
        return iter(self.tags)

    def __getitem__(self, idx: int) -> Tag:
        """Retrieve a Tag at a specified index.

        Args:
            idx (int): The index of the Tag to retrieve.

        Returns:
            Tag: The Tag at the specified index.
        """
        return self.tags[idx]

    def __contains__(self, other: Tag) -> bool:
        """Check if a Tag is in the TagList using binary search.

        Args:
            other (Tag): The Tag to check for presence in the list.

        Returns:
            bool: True if the Tag is in the list, False otherwise.
        """
        idx = bisect_left(self.tags, other)
        return idx < len(self.tags) and self.tags[idx] == other

    def __len__(self) -> int:
        """Return the number of Tags in the TagList.

        Returns:
            int: The number of Tags in the TagList.
        """
        return len(self.tags)

    def __eq__(self, other: object) -> bool:
        """Check equality between two TagLists.

        Args:
            other (object): The object to compare with.

        Raises:
            TagListError: If the other object is not an instance of TagList.

        Returns:
            bool: True if the two TagLists are equal, False otherwise.
        """
        if isinstance(other, TagList):
            tags_are_equal: bool = all(tag_a == tag_b for tag_a, tag_b in zip(self.tags, other.tags))
            lens_are_equal: bool = len(self.tags) == len(other.tags)
            return tags_are_equal and lens_are_equal
        raise TagListError(f'Cannot compare {type(other).__name__} with {self.__class__.__name__}')

    def __repr__(self) -> str:
        """Return a string representation of the TagList.

        Returns:
            str: A string representation of the TagList.
        """
        return f'{self.__class__.__name__}([{", ".join(repr(tag) for tag in self.tags)}])'

    def sort(self) -> None:
        """Sort the list of Tags.

        This method sorts the Tags in the list in ascending order.
        """
        self.tags.sort()

    def add(self, tag: Tag) -> None:
        """Add a Tag to the list if it is not already present.

        Args:
            tag (Tag): The Tag to add to the list.
        """
        if tag not in self:
            self.tags.append(tag)
            self.sort()
