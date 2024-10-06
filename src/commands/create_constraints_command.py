import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.item import Item


class CreateConstraintsCommand(SimpleCommand):
    def __init__(self) -> None:
        """
        Initialize CreateConstraintsCommand
        """
        super().__init__()

    def precondition_check(self, problem: Problem) -> None:
        if problem.config is None:
            raise CommandException(f'{self.__class__.__name__} - Config not loaded')
        if problem.board is None:
            raise CommandException(f'{self.__class__.__name__} - Boad not created')

    def execute(self, problem: Problem) -> None:
        """
        Build the constraints

        :return: None
        """
        super().execute(problem)
        logging.info("Creating Constraints")
        problem.constraints = Item.create(problem.board, {'Constraints': problem.config['Constraints']})

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}()"
