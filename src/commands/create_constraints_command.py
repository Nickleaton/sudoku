"""CreateConstraintsCommand."""
import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.constraints import Constraints


class CreateConstraintsCommand(SimpleCommand):
    """Build the constraints for the problem."""

    def __init__(self, config: str = 'config', board: str = 'board', target: str = 'constraints'):
        """Initialize the CreateConstraintsCommand.

        Args:
            config (str): The key in the problem to find the configuration. Defaults to 'config'.
            board (str): The key in the problem to find the board. Defaults to 'board'.
            target (str): The key where constraints will be added to the problem. Defaults to 'constraints'.
        """
        super().__init__()
        self.config: str = config
        self.board: str = board
        self.target: str = target

    def precondition_check(self, problem: Problem) -> None:
        """Check if the necessary conditions are met before executing the command.

        Args:
            problem (Problem): The problem instance to check conditions on.

        Raises:
            CommandException: If the configuration, board, or target constraints do not meet required conditions.
        """
        if self.config not in problem:
            raise CommandException(f"{self.__class__.__name__} - '{self.config}' configuration missing in problem")
        if self.board not in problem:
            raise CommandException(f"{self.__class__.__name__} - '{self.board}' board not defined in problem")
        if self.target in problem:
            raise CommandException(f"{self.__class__.__name__} - '{self.target}' already exists in the problem")

    def execute(self, problem: Problem) -> None:
        """Execute the command to create constraints.

        Args:
            problem (Problem): The problem instance where constraints will be created and added.

        Returns:
            None
        """
        super().execute(problem)
        logging.info(f"Creating {self.target}")
        problem[self.target] = Constraints.create(problem[self.board],
                                                  {'Constraints': problem[self.config]['Constraints']})

    def __repr__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representation showing configuration, board, and target.
        """
        return f"{type(self).__name__}({self.config!r}, {self.board!r}, {self.target!r})"
