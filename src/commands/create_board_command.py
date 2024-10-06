""" Build Board Command """
import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.board import Board


class CreateBoardCommand(SimpleCommand):

    def __init__(self):
        super().__init__()

    def execute(self, problem: Problem) -> None:
        """
        Build the board
        """
        super().execute(problem)
        logging.info("Creating Board")
        problem.board = Board.create('Board', problem.config)

    def precondition_check(self, problem: Problem) -> None:
        if problem.config is None:
            raise CommandException('config')
