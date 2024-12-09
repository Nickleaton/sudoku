"""CreateConstraintsCommand."""
import pydotted

from src.board.board import Board
from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.constraints import Constraints
from src.items.item import Item


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
        self.input_types: list[KeyType] = [
            KeyType(config, pydotted.pydot),
            KeyType(board, Board),
        ]
        self.output_types: list[KeyType] = [
            KeyType(target, Item),
        ]

    def work(self, problem: Problem) -> None:
        """Execute the command to create constraints.

        Args:
            problem (Problem): The problem instance where constraints will be created and added.
        """
        super().work(problem)
        problem[self.target] = Constraints.create(
            problem[self.board],
            {'Constraints': problem[self.config]['Constraints']},
        )
