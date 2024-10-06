""" Create Problem Command """
import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.item import Item


class CreateProblemCommand(SimpleCommand):

    def __init__(self):
        super().__init__()

    def execute(self, problem: Problem) -> None:
        """
        Create the problem
        """
        logging.info("Creating problem")
        problem.problem = Item.create(problem.board, {'Constraints': problem.config['Constraints']})

    def precondition_check(self, problem: Problem) -> None:
        """
        Check the preconditions for the command.

        :param problem: The problem to check
        :raises CommandException: If the preconditions are not met
        """
        if 'config' not in problem:
            raise CommandException('config')
        if 'board' not in problem is None:
            raise CommandException('board')