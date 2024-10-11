""" Build Board Command """
import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.board import Board


class CreateSolverCommand(SimpleCommand):

    def __init__(self,
                 config: str = 'config',
                 board: str = 'board',
                 target: str = 'solver'
                 ):
        """
        Construct a CreateSolverCommand

        :param config: The attribute of the problem containing the configuration
        :param board: The attribute of the problem containing the board
        :param target: The attribute of the problem to store the solver in
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
            raise CommandException('board')
        if self.target in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.target} already in problem')

    def execute(self, problem: Problem) -> None:
        """
        Build the board
        """
        super().execute(problem)
        logging.info("Creating Board")
        problem.board = Board.create('Board', problem.config)

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        :return: A string representation of the object
        """
        return f'{self.__class__.__name__} - config: {self.config}, board: {self.board}, target: {self.target}'
