"""
Standard composed command.

see https://en.wikipedia.org/wiki/Command_pattern
and https://en.wikipedia.org/wiki/Composite_pattern
"""
from typing import Sequence, List, Optional

from typing_extensions import Self

from src.commands.command import Command
from src.commands.problem import Problem


class ComposedCommand(Command):
    """
    Command built from other commands.
    The class can be iterated.
    """

    def __init__(self, items: Optional[List[Command]] = None):
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
        """
        Checks the preconditions for all the commands in the items list.

        This function iterates over each item in the items list and calls the
        precondition_check method of each item.

        :param problem: The problem to check the preconditions for.
        :raises CommandException: If any of the commands raise a CommandException
            when their preconditions are checked.
        :return: None
        """

        # Pass through is deliberate. We don't want to execute anything here.
        # When the children are executed they will do their precondition checks
        # That matters because some of the commands build data in the problem
        # that gets used in subsequent commands.
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

    def __or__(self, other: Command) -> 'ComposedCommand':
        """
        Combine two commands into a single composed command.

        The `__or__` method implements the logical "or" operator for commands.
        It takes another command as an argument and returns a composed command
        that contains the current command and the other command.

        If the other command is a composed command, its items are added to the
        composed command. Otherwise, the other command is added directly to the
        composed command.

        Example:
            ```
            composed = command1 | command2 | command3
            ```

        :param other: The other command to combine.
        :return: A composed command containing the two commands.
        :rtype: ComposedCommand
        """
        result: ComposedCommand = ComposedCommand(self.items.copy())
        result.add(other)
        return result

    def __iter__(self):
        """
        Returns an iterator object for the composed command.

        :return: The iterator object.
        """
        return iter(self.items)

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
