"""NullCommand."""
import logging

from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class NullCommand(SimpleCommand):
    """A command that does nothing, used as a placeholder."""

    def work(self, problem: Problem) -> None:
        """Execute the command.

        This method logs an info message indicating that the command is being processed.
        As this is a NullCommand, it does not perform any other action.

        Args:
            problem (Problem): The problem to execute the command on.

        Returns:
            None
        """
        super().work(problem)
        logging.info("NullCommand executed.")
