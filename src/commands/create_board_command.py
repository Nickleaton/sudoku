"""
Build Board Command.
"""
import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.board import Board


class CreateBoardCommand(SimpleCommand):
    """
    Command for creating a board from configuration data.
    """

    def __init__(self, source: str = 'config', target: str = 'board'):
        """
        Initializes a CreateBoardCommand instance.

        Args:
            source (str): The attribute in the problem where the configuration is stored.
            target (str): The attribute name in the problem where the board will be stored.
        """
        super().__init__()
        self.source = source
        self.target = target

    def precondition_check(self, problem: Problem) -> None:
        """
        Checks preconditions for the command execution.

        Verifies that the source attribute exists in the problem and that
        the target attribute does not already exist.

        Args:
            problem (Problem): The problem instance to check.

        Raises:
            CommandException: If the source attribute is missing or the target attribute
                              already exists in the problem.
        """
        if self.source not in problem:
            raise CommandException(f"{self.source} not in problem")
        if self.target in problem:
            raise CommandException(f"{self.target} already in problem")

    def execute(self, problem: Problem) -> None:
        """
        Creates the board and stores it in the problem.

        Logs a message indicating that the command is being processed and
        creates a new board in the problem, storing it in the specified target attribute.

        Args:
            problem (Problem): The problem instance to create the board in.
        """
        super().execute(problem)
        logging.info(f"Creating {self.target}")
        problem[self.target] = Board.create('Board', problem[self.source])

    def __repr__(self) -> str:
        """
        Returns a string representation of the CreateBoardCommand instance.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}({self.source!r}, {self.target!r})"
