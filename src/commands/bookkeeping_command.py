import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class BookkeepingCommand(SimpleCommand):
    def __init__(self, constraints: str = 'constraints', target: str = 'bookkeeping_unique'):
        """
        Run the bookkeeping command

        :param constraints: The source attribute for the constraints
        :param target: The name of the attribute to store if the bookkeeping is unique
        """
        super().__init__()
        self.constraints: str = constraints
        self.target: str = target

    def precondition_check(self, problem: Problem) -> None:
        """
        Check the preconditions for the command.

        :param problem: The problem to check
        :raises CommandException: If the preconditions are not met
        """
        if self.constraints not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.constraints} does not exist in the problem')
        if self.target in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.target} already exists in the problem')

    def execute(self, problem: Problem) -> None:
        """
        Do the bookkeeping

        :return: None
        """
        super().execute(problem)
        logging.info(f"Creating {self.target}")
        problem[self.constraints].bookkeeping()
        problem[self.target] = problem[self.constraints].bookkeeping_unique()

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}({self.constraints!r}, {self.target!r})"
