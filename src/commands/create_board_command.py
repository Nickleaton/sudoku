"""CreateBoardCommand."""
import logging

import pydotted

from src.board.board import Board
from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class CreateBoardCommand(SimpleCommand):
    """Command to create start board from configuration line."""

    def __init__(self, source: str = 'config', target: str = 'board'):
        """Initialize start CreateBoardCommand instance.

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
            KeyType(target, Board),
        ]

    def work(self, problem: Problem) -> None:
        """Create the board and store it in the problem.

        Log start message indicating that the command is being processed and
        create start new board in the problem, storing it in the specified target attribute.

        Args:
            problem (Problem): Problem instance to create the board in.
        """
        super().work(problem)
        logging.info(f'Creating {self.target}')
        problem[self.target] = Board.create('Board', problem[self.source])
