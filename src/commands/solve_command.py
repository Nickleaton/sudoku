"""Base for different solvers."""
import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class SolveCommand(SimpleCommand):
    """Command to solve a problem using a specified solver."""

    def __init__(self, solver: str = 'solver', target: str = 'solution', log: str = 'log'):
        """Construct a SolveCommand.

        Args:
            solver (str): The field containing the solver to use.
            target (str): The field to store the solution in.
            log (str): The field to store the log of the solver.
        """
        super().__init__()
        self.solver = solver
        self.target = target
        self.log = log

    def precondition_check(self, problem: Problem) -> None:
        """Check the preconditions for the command.

        Args:
            problem (Problem): The problem to check.

        Raises:
            CommandException: If the preconditions are not met.
        """
        if self.solver not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.solver} not created')
        if self.target in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.target} already in problem')

    def execute(self, problem: Problem) -> None:
        """Solve the puzzle.

        Args:
            problem (Problem): The problem to solve.
        """
        super().execute(problem)
        logging.info(f"Solving {self.solver} and storing solution in {self.target}")
        problem[self.solver].solve()
        problem[self.target] = problem[self.solver].answer
        # Handle log

    def __repr__(self) -> str:
        """Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f'{self.__class__.__name__}({self.solver!r}, {self.target!r}, {self.log!r})'
