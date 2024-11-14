"""NullCommand."""
import logging

from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class NullCommand(SimpleCommand):
    """A command that does nothing, used as a placeholder."""

    def execute(self, problem: Problem) -> None:
        """Execute the command.

        This method logs an info message indicating that the command is being processed.
        As this is a NullCommand, it does not perform any other action.

        Args:
            problem (Problem): The problem to execute the command on.

        Returns:
            None
        """
        super().execute(problem)
        logging.info("NullCommand executed.")

    def __repr__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representation of the NullCommand object.
        """
        return f"{self.__class__.__name__}()"
