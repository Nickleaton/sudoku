"""Tag List"""
from typing import List

from src.utils.tag import Tag


class TagListException(Exception):
    """ Exception when using TagList """
    pass


class TagList:
    """ List of Tags """
    def __init__(self, items: List[Tag]):
        """
        Construct a tag list
        :param items: List of tags
        """
        self.items = items
        self.sort()
        self.n = 0

    def __iter__(self) -> 'TagList':
        self.n = 0
        return self

    def __next__(self) -> 'Tag':
        if self.n < len(self):
            result = self.items[self.n]
            self.n += 1
        else:
            raise StopIteration
        return result

    def __contains__(self, other: Tag) -> bool:
        for item in self.items:
            if item == other:
                return True
        return False

    def __len__(self) -> int:
        return len(self.items)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, TagList):
            if len(self.items) != len(other.items):
                return False
            for i, o in zip(self.items, other.items):
                if i != o:
                    return False
            return True
        raise TagListException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}([{', '.join([repr(v) for v in self.items])}])"

    def sort(self) -> None:
        """"
        Sort the list of tags by tag priority
        """
        self.items = sorted(self.items)

    def add(self, item: Tag) -> None:
        """
        Add a tag to the list if it is not already there
        :param item: Item to add
        """
        if item not in self:
            self.items.append(item)
        self.sort()
