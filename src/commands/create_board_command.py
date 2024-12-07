"""CreateBoardCommand."""
import logging

import pydotted

from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.board import Board


class CreateBoardCommand(SimpleCommand):
    """Command to create a board from configuration data."""

    def __init__(self, source: str = 'config', target: str = 'board'):
        """Initialize a CreateBoardCommand instance.

        Args:
            source (str): Attribute in the problem where the configuration is stored.
            target (str): Attribute name in the problem where the board will be stored.
        """
        super().__init__()
        self.source = source
        self.target = target
        self.input_types: list[KeyType] = [
            KeyType(source, pydotted.pydot),
        ]
        self.output_types: list[KeyType] = [
            KeyType(target, Board)
        ]

    def work(self, problem: Problem) -> None:
        """Create the board and store it in the problem.

        Log a message indicating that the command is being processed and
        create a new board in the problem, storing it in the specified target attribute.

        Args:
            problem (Problem): Problem instance to create the board in.
        """
        super().work(problem)
        logging.info(f"Creating {self.target}")
        problem[self.target] = Board.create('Board', problem[self.source])
