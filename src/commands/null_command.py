"""NullCommand module."""

import logging

from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class NullCommand(SimpleCommand):
    """A command that performs no action, used as a placeholder."""

    def work(self, problem: Problem) -> None:
        """Log a message indicating the command execution.

        Executes the `NullCommand`, which logs an informational message.
        This command serves as a placeholder and does not alter the problem.

        Args:
            problem (Problem): The problem instance on which the command is executed.
        """
        super().work(problem)
        logging.info('NullCommand executed.')
