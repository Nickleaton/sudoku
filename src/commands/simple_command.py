"""SimpleCommand."""
from src.commands.command import Command
from src.commands.composed_command import ComposedCommand


class SimpleCommand(Command):
    """Base class for simple commands."""

    def __or__(self, other: 'Command') -> ComposedCommand:
        """Combine two commands into a single composed command.

        The `__or__` method implements the logical "or" operator for commands.
        It takes another command as an argument and returns a composed command
        that contains the current command and the other command.

        Args:
            other (Command): The other command to combine.

        Returns:
            ComposedCommand: A composed command containing the two commands.
        """
        result: ComposedCommand = ComposedCommand()
        result.add(self)
        if isinstance(other, ComposedCommand):
            result.add_items(other.items)
        else:
            result.add(other)
        return result
