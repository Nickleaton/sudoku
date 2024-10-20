""" Command base class.

Commands are used to do the actual work.
Based on the Command pattern from the Gang of Four book
https://en.wikipedia.org/wiki/Command_pattern
"""
import logging
from abc import ABC

from src.commands.problem import Problem
from src.utils.sudoku_exception import SudokuException


class CommandException(SudokuException):
    """  Raised when there is an error in a command. """

    def __init__(self, attribute: str):
        """
        Initialize a CommandException.

        :param attribute: The attribute of the problem which caused the error.
        """
        super().__init__(f"Error in {attribute}")
        self.attribute = attribute


class Command(ABC):
    """
    Base class for all commands.
    Implements the Command pattern from the Gang of Four book
    """

    def __init__(self):
        """ Command base class. """
        pass

    @property
    def name(self) -> str:
        """
        Get the name of the class in a readable form.

        Returns:
            str: The name of the class.
        """

        return self.__class__.__name__.replace("Command", "") if self.__class__.__name__ != 'Command' else 'Command'

    def precondition_check(self, problem: Problem) -> None:
        """
        Check the preconditions for the command.

        This method checks that the preconditions for the command are met.
        The preconditions may be different for each command and are determined
        by the command's implementation.

        :param problem: The problem to check
        :raises CommandException: If the preconditions are not met
        """
        pass

    def execute(self, problem: Problem) -> None:
        """
        Execute the command.

        This method performs the actual work of the command. It logs an info message
        indicating that the command is being processed.

        Returns:
            None
        """
        logging.info(f"{self.__class__.__name__} process")
        self.precondition_check(problem)

    def __repr__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}()"
