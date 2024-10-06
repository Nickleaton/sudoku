from typing import Self

from src.commands.command import Command
from src.commands.composed_command import ComposedCommand


class SimpleCommand(Command):

    def __init__(self):
        super().__init__()

    def __or__(self, other: Self) -> ComposedCommand:
        """
        Create a composed command that contains the current command and the given command.

        This method returns a new ComposedCommand that contains the current command and the given command.
        If the given command is a ComposedCommand, its items are added to the new command.

        Args:
            other (Self): The other command to add to the composed command.

        Returns:
            Self: A new ComposedCommand that contains the current command and the given command.
        """
        result: ComposedCommand = ComposedCommand()
        result.add(self)
        if isinstance(other, ComposedCommand):
            result.add_items(other.items)
        else:
            result.add(other)
        return result