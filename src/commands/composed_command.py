"""Standard composed command.

For more information, see:
- https://en.wikipedia.org/wiki/Command_pattern
- https://en.wikipedia.org/wiki/Composite_pattern
"""
from typing import Sequence

from src.commands.command import Command
from src.commands.problem import Problem


class ComposedCommand(Command):
    """Combine multiple commands."""

    def __init__(self, items: list[Command] | None = None):
        """Initialize a new instance of the ComposedCommand class.

        Args:
            items (list[Command], optional): A list of commands to initialize
                in the composed command. Defaults to an empty list.
        """
        super().__init__()
        self.items: list[Command] = items if items is not None else []

    def add(self, item: Command) -> None:
        """Add a command to the composed command.

        Args:
            item (Command): The command to add.
        """
        self.items.append(item)

    def add_items(self, items: Sequence[Command]) -> None:
        """Add multiple commands to the composed command.

        Args:
            items (Sequence[Command]): A sequence of commands to add.
        """
        for item in items:
            self.add(item)

    def execute(self, problem: Problem) -> None:
        """Execute all commands in the composed command sequentially.

        Args:
            problem (Problem): The problem instance to execute the commands on.
        """
        super().execute(problem)
        for item in self.items:
            item.execute(problem)

    def __or__(self, other: Command) -> 'ComposedCommand':
        """Combine two commands into a new composed command.

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
        """Return an iterator for the composed command.

        Returns:
            Iterator[Command]: An iterator over the commands in the composed command.
        """
        return iter(self.items)

    def __len__(self) -> int:
        """Return the number of commands in the composed command.

        Returns:
            int: The number of commands.
        """
        return len(self.items)

    def __repr__(self) -> str:
        """Return a string representation of the composed command.

        Returns:
            str: A representation of the composed command with its items.
        """
        return f"{self.__class__.__name__}([{', '.join([repr(item) for item in self])}])"
