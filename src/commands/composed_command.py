from typing import Sequence, List, Optional

from src.commands.command import Command


class ComposedCommand(Command):

    def __init__(self, output_filename: str, items: Sequence[Command]):
        super().__init__(output_filename)
        self.items: List[Command] = []
        self.add_items(items)

    def process(self) -> None:
        for item in self.items:
            item.process()

    def write(self) -> None:
        for item in self.items:
            item.write()

    def add(self, item: Command):
        self.items.append(item)
        item.parent = self

    def add_items(self, items: Sequence[Command]):
        for item in items:
            self.add(item)

    def __iter__(self):
        self._n = 0
        return self

    def __next__(self) -> Optional[Command]:
        if self._n < len(self.items):
            result = self.items[self._n]
            self._n += 1
            return result
        self._n = 0
        raise StopIteration

    def __len__(self) -> int:
        return len(self.items)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.output_filename}', [{', '.join([repr(item) for item in self])}])"
