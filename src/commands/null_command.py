import logging

from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class NullCommand(SimpleCommand):
    def __init__(self):
        """
        Construct a NullCommand.

        This command does nothing and is used to indicate
        where a command should be inserted in a composed command
        """
        super().__init__()

    def execute(self, problem: Problem):
        """
        Execute the command.

        This method performs the actual work of the command. It logs an info message
        indicating that the command is being processed.

        Parameters:
            problem (Problem): The problem to execute the command on.

        Returns:
            None
        """
        super().execute(problem)
        logging.info("NullCommand")

    def precondition_check(self, problem: Problem) -> None:
        """
        Check the preconditions for the command.

        This method is a no-op and exists solely to fulfill the abstract
        base class requirement of the SimpleCommand class. NullCommand does
        not have any preconditions.

        Parameters:
            problem (Problem): The problem to check

        Returns:
            None
        """
        pass

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}()"
