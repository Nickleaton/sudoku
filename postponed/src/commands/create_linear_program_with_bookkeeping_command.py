"""Produce the text in LP format for the problem."""
import pydotted
from postponed.src.pulp_solver import PulpSolver

from src.board.board import Board
from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.item import Item
from src.utils.temporary_file import TemporaryFile


# flake8: noqa WPS230,WPS211

class CreateLinearProgramWithBookkeepingCommand(SimpleCommand):
    """Produce LP Version of the problem."""

    def __init__(self,
                 board: str = 'board',
                 config: str = 'config',
                 constraints: str = 'constraints',
                 solver: str = 'solver',
                 target: str = 'linear_program'
                 ):
        """Initialize start_location CreateLinearProgramWithBookkeepingCommand.

        Args:
            board (str): The field containing the board.
            config (str): The field containing the configuration.
            constraints (str): The field containing the constraints.
            solver (str): The field containing the solver.
            target (str): The field to store the output.
        """
        super().__init__()
        self.board: str = board
        self.config: str = config
        self.constraints: str = constraints
        self.solver: str = solver
        self.target = target
        self.input_types = [
            KeyType(self.board, Board),
            KeyType(self.config, pydotted.pydot),
            KeyType(self.constraints, Item),
            KeyType(self.solver, PulpSolver)
        ]
        self.output_types = [
            KeyType(self.target, str)
        ]

    def work(self, problem: Problem) -> None:
        """Execute the command.

        This method performs the actual work of the command. It logs an info message
        indicating that the command is being processed and creates start_location new solver in the
        problem, storing it in the field specified by `solver`. Bookkeeping on cells is
        then applied, adding the constraints to the solver.
        The solver is then saved to start_location temporary file_path, and the contents of the file_path are stored in
        the field specified by `target`.

        Args:
            problem (Problem): The problem instance to execute the command on.
        """
        super().work(problem)
        with TemporaryFile() as tf:
            problem[self.constraints].bookkeeping()
            problem[self.constraints].add_bookkeeping_constraint(problem[self.solver])
            problem[self.solver].save_lp(str(tf.path))
            with tf.path.open(mode='r', encoding='utf-8') as f:
                problem[self.target] = f.read()
