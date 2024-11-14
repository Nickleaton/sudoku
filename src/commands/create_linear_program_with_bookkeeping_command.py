"""Produce the text in LP format for the problem."""
import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.temporary_file import TemporaryFile


class CreateLinearProgramWithBookkeepingCommand(SimpleCommand):
    """Produce LP Version of the problem."""

    def __init__(self,
                 board: str = 'board',
                 config: str = 'config',
                 constraints: str = 'constraints',
                 solver: str = 'solver',
                 target: str = 'linear_program'
                 ):
        """Initialize a CreateLinearProgramWithBookkeepingCommand.

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

    def precondition_check(self, problem: Problem) -> None:
        """Check the preconditions for the command.

        Args:
            problem (Problem): The problem to check.

        Raises:
            CommandException: If any of the preconditions are not met.
        """
        if self.config not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.config} not loaded')
        if self.board not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.board} not built')
        if self.constraints not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.constraints} not built')
        if self.solver not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.solver} not built')
        if self.target in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.target} already in problem')

    def execute(self, problem: Problem) -> None:
        """Execute the command.

        This method performs the actual work of the command. It logs an info message
        indicating that the command is being processed and creates a new solver in the
        problem, storing it in the field specified by `solver`. Bookkeeping on cells is
        then applied, adding the constraints to the solver.
        The solver is then saved to a temporary file, and the contents of the file are stored in
        the field specified by `target`.

        Args:
            problem (Problem): The problem instance to execute the command on.
        """
        super().execute(problem)
        logging.info(f"Creating {self.target}")
        with TemporaryFile() as _:
            problem[self.constraints].bookkeeping()
            # TODO
            problem[self.constraints].add_bookkeeping_constraint(problem[self.solver])
            with TemporaryFile() as tf:
                problem[self.solver].save_lp(str(tf.path))
                with tf.path.open(mode='r', encoding='utf-8') as f:
                    problem[self.target] = f.read()

    def __repr__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return (
            f"{self.__class__.__name__}"
            f"("
            f"{self.board!r}, "
            f"{self.config!r}, "
            f"{self.constraints!r}, "
            f"{self.solver!r}, "
            f"{self.target!r}"
            f")"
        )
