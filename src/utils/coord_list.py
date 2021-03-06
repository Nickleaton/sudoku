from typing import List

from src.utils.coord import Coord


class CoordListException(Exception):
    pass


class CoordList:

    def __init__(self, items: List[Coord]):
        self.items = items
        self.sort()
        self.n = 0

    def __iter__(self) -> 'CoordList':
        self.n = 0
        return self

    def __next__(self) -> Coord:
        if self.n < len(self):
            result = self.items[self.n]
            self.n += 1
        else:
            raise StopIteration
        return result

    def __contains__(self, other: Coord) -> bool:
        for item in self.items:
            if item == other:
                return True
        return False

    def __len__(self) -> int:
        return len(self.items)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, CoordList):
            if len(self.items) != len(other.items):
                return False
            for i, o in zip(self.items, other.items):
                if i != o:
                    return False
            return True
        raise CoordListException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}([{', '.join([repr(v) for v in self.items])}])"

    def sort(self) -> None:
        self.items = sorted(self.items)

    def add(self, item: Coord) -> None:
        if item not in self:
            self.items.append(item)
        self.sort()
