from typing import List

from src.utils.coord import Coord
from src.utils.tag import Tag


class TagList:

    def __init__(self, items: List[Tag]):
        self.items = []
        for item in items:
            self.add(item)
        self.sort()

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self):
            result = self.items[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __contains__(self, other: Tag) -> bool:
        for item in self:
            if item == other:
                return True
        return False

    def __len__(self) -> int:
        return len(self.items)

    def __eq__(self, other: 'TagList') -> bool:
        if len(self.items) != len(other.items):
            return False
        for i, o in zip(self.items, other.items):
            if i != o:
                return False
        return True

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}([{', '.join([repr(v) for v in self.items])}])"

    def sort(self):
        self.items = sorted(self.items)

    def add(self, item: Tag) -> None:
        if item not in self:
            self.items.append(item)
        self.sort()
