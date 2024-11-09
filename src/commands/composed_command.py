"""
Standard composed command.

For more information, see:
- https://en.wikipedia.org/wiki/Command_pattern
- https://en.wikipedia.org/wiki/Composite_pattern
"""
from typing import Sequence, List, Optional

from src.commands.command import Command
from src.commands.problem import Problem


class ComposedCommand(Command):
    """
    Command that combines multiple other commands, allowing them to be executed
    as a single unit. Supports iteration and combination with the logical "or" operator.
    """

    def __init__(self, items: Optional[List[Command]] = None):
        """
        Initializes a new instance of the ComposedCommand class.

        Args:
            items (List[Command], optional): A list of commands to initialize
                in the composed command. Defaults to an empty list.
        """
        super().__init__()
        self.items: List[Command] = items if items is not None else []

    def add(self, item: Command) -> None:
        """
        Adds a command to the composed command.

        Args:
            item (Command): The command to add.
        """
        self.items.append(item)

    def add_items(self, items: Sequence[Command]) -> None:
        """
        Adds multiple commands to the composed command.

        Args:
            items (Sequence[Command]): A sequence of commands to add.
        """
        for item in items:
            self.add(item)

    def execute(self, problem: Problem) -> None:
        """
        Executes all commands in the composed command sequentially.

        Args:
            problem (Problem): The problem instance to execute the commands on.
        """
        super().execute(problem)
        for item in self.items:
            item.execute(problem)

    def __or__(self, other: Command) -> 'ComposedCommand':
        """
        Combines two commands into a new composed command.

        Args:
            other (Command): The other command to combine with.

        Returns:
            ComposedCommand: A new composed command containing both commands.

        Example:
            ```
            composed = command1 | command2 | command3
            ```
        """
        result: ComposedCommand = ComposedCommand(self.items.copy())
        result.add(other)
        return result

    def __iter__(self):
        """
        Returns an iterator for the composed command.

        Returns:
            Iterator[Command]: An iterator over the commands in the composed command.
        """
        return iter(self.items)

    def __len__(self) -> int:
        """
        Returns the number of commands in the composed command.

        Returns:
            int: The number of commands.
        """
        return len(self.items)

    def __repr__(self) -> str:
        """
        Returns a string representation of the composed command.

        Returns:
            str: A representation of the composed command with its items.
        """
        return f"{self.__class__.__name__}([{', '.join([repr(item) for item in self])}])"
