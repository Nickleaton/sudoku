import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.item import Item


class CreateConstraintsCommand(SimpleCommand):
    def __init__(self, config: str = 'config', board: str = 'board', target: str = 'constraints'):
        """
        Construct a CreateConstraintsCommand.

        :param source: The source attribute to use to build the constraints
        :param target: The name of the attribute to store the constraints in
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
            raise CommandException(f'{self.__class__.__name__} - {self.target} does not exist in the problem')
        if self.board not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.board} does not exist in the problem')
        if self.target in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.target} already exists in the problem')

    def execute(self, problem: Problem) -> None:
        """
        Build the constraints.

        :return: None
        """
        super().execute(problem)
        logging.info(f"Creating {self.target}")
        problem[self.target] = Item.create(problem[self.board], {'Constraints': problem[self.config]['Constraints']})

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}({self.config!r}, {self.board!r}, {self.target!r})"
