"""Command base class.

Commands are used to perform specific actions following the Command pattern
from the Gang of Four book.
For more information, see https://en.wikipedia.org/wiki/Command_pattern
"""
import logging

from src.commands.problem import Problem
from src.utils.sudoku_exception import SudokuException


class CommandException(SudokuException):
    """Raise when an error occurs in a command.

    Attributes:
        attribute (str): The attribute of the problem that caused the error.
    """

    def __init__(self, attribute: str):
        """Initialize a CommandException.

        Args:
            attribute (str): The attribute of the problem that caused the error.
        """
        super().__init__(f"Error in {attribute}")
        self.attribute = attribute


class Command:
    """Define a base class for all commands implementing the Command pattern.

    Commands inheriting from this base class should define specific behavior
    in their `execute` and `precondition_check` methods.
    """

    @property
    def name(self) -> str:
        """Return a readable name for the command class.

        Returns:
            str: The name of the class, with "Command" removed if present.
        """
        return self.__class__.__name__.replace("Command", "") if self.__class__.__name__ != 'Command' else 'Command'

    def precondition_check(self, problem: Problem) -> None:
        """Check that the preconditions for the command are met.

        Override this method in subclasses to define specific
        preconditions. Raise a `CommandException` if conditions are not met.

        Args:
            problem (Problem): The problem instance to check.

        Raises:
            CommandException: If the preconditions are not met.
        """

    def execute(self, problem: Problem) -> None:
        """Execute the command, performing the specified action.

        Log an info message indicating that the command is being processed
        and check preconditions by calling `precondition_check`.

        Args:
            problem (Problem): The problem instance to execute the command on.

        Returns:
            None
        """
        logging.info(f"{self.__class__.__name__} process")
        self.precondition_check(problem)

    def __repr__(self):
        """Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}()"
