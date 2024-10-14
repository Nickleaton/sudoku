from src.commands.command import Command
from src.commands.composed_command import ComposedCommand
from src.commands.problem import Problem


class SimpleCommand(Command):

    def __init__(self):
        super().__init__()

    def execute(self, problem: Problem) -> None:
        super().execute(problem)

    def __or__(self, other: 'Command') -> ComposedCommand:
        """
        Combine two commands into a single composed command.

        The `__or__` method implements the logical "or" operator for commands.
        It takes another command as an argument and returns a composed command
        that contains the current command and the other command.

        If the other command is a composed command, its items are added to the
        composed command. Otherwise, the other command is added directly to the
        composed command.

        :param other: The other command to combine.
        :return: A composed command containing the two commands.
        :rtype: ComposedCommand
        """
        result: ComposedCommand = ComposedCommand()
        result.add(self)
        if isinstance(other, ComposedCommand):
            result.add_items(other.items)
        else:
            result.add(other)
        return result
