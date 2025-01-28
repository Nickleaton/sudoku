"""ExtractAnswerCommand."""
import logging
from itertools import product

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.commands.solve_command import SolveCommand
from src.solvers.answer import Answer
from src.solvers.solver_status import SolverStatus
from src.solvers.variables import Variables


class ExtractAnswerCommand(SimpleCommand):
    """Command for extracting the line from the solver's results."""

    def __init__(self):
        """Initialize an ExtractAnswerCommand instance."""
        super().__init__()
        self.add_preconditions([SolveCommand])

    def work(self, problem: Problem) -> None:
        """Extract the line from the solver's results and store it in the problem.

        If the solver's status is not optimal, the command will not store any line.

        Args:
            problem (Problem): The problem instance from which to extract the line.

        Raises:
            CommandException: If the solver's status is not optimal.
            CommandException: If the board is not created.
            CommandException: If the solver is not created.
        """
        if problem.status is None:
            raise CommandException('No solve has been performed.')
        if problem.board is None:
            raise CommandException('No board has been created.')
        if problem.solver is None:
            raise CommandException('No solver has been created.')
        if problem.status != SolverStatus.optimal:
            logging.warning('The solver did not find an optimal solution.')
            return

        problem.answer = Answer(problem.board)
        variables: Variables = problem.solver.variables
        for row, column in product(problem.board.row_range, problem.board.column_range):
            number: int = int(variables.numbers[row, column].varValue)
            problem.answer[row, column] = number
