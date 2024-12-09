"""CreateLinearProgramCommand."""
import logging

import pydotted

from src.board.board import Board
from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.item import Item
from src.solvers.solver import Solver
from src.utils.temporary_file import TemporaryFile


# flake8: noqa WPS230,WPS211

class CreateLinearProgramCommand(SimpleCommand):
    """Produce the LP version of the problem."""

    def __init__(self,
                 board: str = 'board',
                 config: str = 'config',
                 constraints: str = 'constraints',
                 solver: str = 'solver',
                 target: str = 'linear_program',
                 ):
        """Initialize CreateLinearProgramCommand.

        Args:
            board (str): Field containing the board. Defaults to 'board'.
            config (str): Field containing the configuration. Defaults to 'config'.
            constraints (str): Field containing the constraints. Defaults to 'constraints'.
            solver (str): Field containing the solver. Defaults to 'solver'.
            target (str): Field to store the output. Defaults to 'linear_program'.
        """
        super().__init__()
        self.board: str = board
        self.config: str = config
        self.constraints: str = constraints
        self.solver: str = solver
        self.target: str = target
        self.input_types = [
            KeyType(self.config, pydotted.pydot),
            KeyType(self.board, Board),
            KeyType(self.constraints, Item),
            KeyType(self.solver, Solver),
        ]
        self.output_types = [
            KeyType(self.target, str),
        ]

    def work(self, problem: Problem) -> None:
        """Produce the LP version of the problem.

        Logs start message indicating that the command is being processed. Creates a new LP solver
        in the problem, stores it in the field specified by `self.solver`, and saves the LP output
        to a temporary file. The text of that file is then stored in the field specified by `self.target`.

        Args:
            problem (Problem): The problem instance to create the LP version of.
        """
        super().work(problem)
        logging.info(f'Creating {self.target}')
        with TemporaryFile() as tf:
            problem[self.solver].save_lp(str(tf.path))
            with tf.path.open(mode='r', encoding='utf-8') as lp_file:
                problem[self.target] = lp_file.read()
