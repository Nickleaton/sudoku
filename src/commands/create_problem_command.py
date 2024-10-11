""" Create Problem Command """
import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.item import Item


class CreateProblemCommand(SimpleCommand):

    def __init__(self,
                 config: str = 'config',
                 board: str = 'board',
                 target: str = 'problem'
                 ):
        """
        Initialize a CreateProblemCommand object.

        Parameters:
            config (str): The field in the problem containing the configuration
            board (str): The field in the problem containing the board
            target (str): The field in the problem to create.
        """
        super().__init__()
        self.config: str = config
        self.board: str = board
        self.target: str = target

    def precondition_check(self, problem: Problem) -> None:
        """
        Check the preconditions for the command.

        :param problem: The problem to check
        :raises CommandException: If the preconditions are not met
        """
        if self.config not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.config} not loaded')
        if self.board not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.board} not loaded')
        if self.target in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.target} already in problem')

    def execute(self, problem: Problem) -> None:
        """
        Create the problem
        """
        logging.info(f"Creating {self.target}")
        problem.problem = Item.create(problem[self.board], {'Constraints': problem[self.config]['Constraints']})

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f'{self.__class__.__name__}({self.config}, {self.board}, {self.target})'