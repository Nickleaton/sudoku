"""TagList."""
from bisect import bisect_left
from typing import Iterator

from src.utils.tag import Tag


class TagListError(Exception):
    """Exception raised for errors related to TagList operations."""


class TagList:
    """A list of Tags with methods for managing and sorting them."""

    def __init__(self, tags: list[Tag] | None = None):
        """Initialize a TagList with an optional list of Tags."""
        self.tags = list(tags) if tags else []
        self.sort()

    def __iter__(self) -> Iterator[Tag]:
        """Return an iterator for the TagList."""
        return iter(self.tags)

    def __getitem__(self, idx: int) -> Tag:
        """Retrieve a Tag at a specified index."""
        return self.tags[idx]

    def __contains__(self, other: Tag) -> bool:
        """Check if a Tag is in the TagList using binary search."""
        idx = bisect_left(self.tags, other)
        return idx < len(self.tags) and self.tags[idx] == other

    def __len__(self) -> int:
        """Return the number of Tags in the TagList."""
        return len(self.tags)

    def __eq__(self, other: object) -> bool:
        """Check equality between two TagLists."""
        if isinstance(other, TagList):
            return len(self.tags) == len(other.tags) and all(a == b for a, b in zip(self.tags, other.tags))
        raise TagListError(f'Cannot compare {type(other).__name__} with {self.__class__.__name__}')

    def __repr__(self) -> str:
        """Return a string representation of the TagList."""
        return f'{self.__class__.__name__}([{", ".join(repr(tag) for tag in self.tags)}])'

    def sort(self) -> None:
        """Sort the list of Tags."""
        self.tags.sort()

    def add(self, tag: Tag) -> None:
        """Add a Tag to the list if it is not already present."""
        if tag not in self:
            self.tags.append(tag)
            self.sort()
