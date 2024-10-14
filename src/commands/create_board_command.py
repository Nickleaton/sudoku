""" Build Board Command """
import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.board import Board


class CreateBoardCommand(SimpleCommand):

    def __init__(self, source: str = 'config', target: str = 'board'):
        super().__init__()
        self.source = source
        self.target = target

    def precondition_check(self, problem: Problem) -> None:
        """
        Check the preconditions for the command.

        :param problem: The problem to check
        :raises CommandException: If the preconditions are not met
        """
        if self.source not in problem is None:
            raise CommandException(f"{self.source} not in problem")
        if self.target in problem:
            raise CommandException(f"{self.target} already in problem")

    def execute(self, problem: Problem) -> None:
        """
        Create the board.

        This method performs the actual work of the command. It logs an info message
        indicating that the command is being processed and creates a new board in the
        problem, storing it in the field specified by `target`.

        Parameters:
            problem (Problem): The problem to create the board in.

        Returns:
            None
        """
        super().execute(problem)
        logging.info(f"Creating {self.target}")
        problem[self.target] = Board.create('Board', problem[self.source])

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}({self.source!r}, {self.target!r})"
