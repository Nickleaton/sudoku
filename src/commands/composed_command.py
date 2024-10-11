""" Standard composed command

see https://en.wikipedia.org/wiki/Command_pattern
and https://en.wikipedia.org/wiki/Composite_pattern
"""
from typing import Sequence, List, Optional, Self

from src.commands.command import Command
from src.commands.problem import Problem


class ComposedCommand(Command):
    """ Command built from other commands
    The class can be iterated
    """

    def __init__(self, items: List[Command] = None):
        """
        Initializes a new instance of the ComposedCommand class.

        This method sets up the command by calling the base class's __init__ method and initializing
        an empty list of commands.

        Args:
            items (List[Command], optional): A list of commands to be added to the
                items list. Defaults to an empty list.

        Returns:
            None
        """
        super().__init__()
        self.items: List[Command] = items if items is not None else []

    def add(self, item: Command) -> None:
        """
        Adds a command to the list of items and sets the parent of the item.

        :param item: The command to add to the list of items.
        :return: None
        """

        self.items.append(item)

    def add_items(self, items: Sequence[Command]) -> None:
        """
        Bulk adds a list of commands to the composed command.

        :param items: A sequence of commands to add to the composed command.
        :return: None
        """
        for item in items:
            self.add(item)

    def precondition_check(self, problem: Problem) -> None:
        pass

    def execute(self, problem: Problem) -> None:
        """
        Executes all the commands in the items list.

        This function iterates over each item in the items list and calls the execute
        method of each item.

        Returns:
            None
        """
        super().execute(problem)
        for item in self.items:
            item.execute(problem)

    def __or__(self, other: Command) -> Self:
        self.add(other)
        return self

    def __iter__(self):
        """
        Returns an iterator object for the composed command.

        :return: The iterator object.
        """
        return iter(self.items)

    def __next__(self) -> Optional[Command]:
        """
        Returns the next command in the sequence.

        :return: The next command in the sequence, or None if the sequence has been exhausted.
        """
        if self._n < len(self.items):
            result = self.items[self._n]
            self._n += 1
            return result
        self._n = 0
        raise StopIteration

    def __len__(self) -> int:
        """
        Returns the number of items in the composed command.

        :return: The number of items in the composed command.
        """
        return len(self.items)

    def __repr__(self) -> str:
        """
        Returns a string representation of the object, including its class name and a list of its items.
        """
        return f"{self.__class__.__name__}([{', '.join([repr(item) for item in self])}])"
