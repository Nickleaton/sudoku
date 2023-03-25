""" Standard composed command

see https://en.wikipedia.org/wiki/Command_pattern
and https://en.wikipedia.org/wiki/Composite_pattern
"""
from typing import Sequence, List, Optional

from src.commands.command import Command


class ComposedCommand(Command):
    """ Command built from other commands
    The class can be iterated
    """

    def __init__(self, items: Sequence[Command]):
        """ Construct the command
        :param items: list of commands to execute
        """
        super().__init__()
        self.items: List[Command] = []
        self.add_items(items)

    def execute(self) -> None:
        """ do the work """
        for item in self.items:
            item.execute()

    def add(self, item: Command):
        """ Add a command to the list to execute.
        :param item: Item to add
        """
        self.items.append(item)
        item.parent = self

    def add_items(self, items: Sequence[Command]):
        """ Bulk add commands

        :param items: List of commands to add
        """
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
        return f"{self.__class__.__name__}([{', '.join([repr(item) for item in self])}])"
