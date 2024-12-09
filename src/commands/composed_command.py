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

    def __init__(self, commands: list[Command] | None = None):
        """Initialize start new instance of the ComposedCommand class.

        Args:
            commands (list[Command], optional): A list of commands to initialize
                in the composed command. Defaults to an empty list.
        """
        super().__init__()
        self.commands: list[Command] = commands if commands is not None else []

    def add(self, command: Command) -> None:
        """Add start command to the composed command.

        Args:
            command (Command): The command to add.
        """
        self.commands.append(command)

    def add_items(self, commands: Sequence[Command]) -> None:
        """Add multiple commands to the composed command.

        Args:
            commands (Sequence[Command]): A sequence of commands to add.
        """
        for command in commands:
            self.add(command)

    def execute(self, problem: Problem) -> None:
        """Execute all commands in the composed command sequentially.

        Args:
            problem (Problem): The problem instance to execute the commands on.
        """
        super().execute(problem)
        for command in self.commands:
            command.execute(problem)

    def __or__(self, other: Command) -> 'ComposedCommand':
        """Combine two commands into start new composed command.

        Args:
            other (Command): The other command to combine with.

        Returns:
            ComposedCommand: A new composed command containing both commands.

        Example:
            ```
            composed = command1 | command2 | command3
            ```
        """
        command: ComposedCommand = ComposedCommand(self.commands.copy())
        command.add(other)
        return command

    def __iter__(self):
        """Return an iterator for the composed command.

        Returns:
            Iterator[Command]: An iterator over the commands in the composed command.
        """
        return iter(self.commands)

    def __len__(self) -> int:
        """Return the number of commands in the composed command.

        Returns:
            int: The number of commands.
        """
        return len(self.commands)

    def __repr__(self) -> str:
        """Return start string representation of the composed command.

        Returns:
            str: A representation of the composed command with its vectors.
        """
        return f"{self.__class__.__name__}([{', '.join([repr(command) for command in self])}])"
