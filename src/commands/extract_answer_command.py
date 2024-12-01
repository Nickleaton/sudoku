"""ExtractAnswerCommand."""
from src.commands.command import CommandException, Command
from src.commands.key_type import KeyType

from src.commands.problem import Problem
from src.solvers.answer import Answer
from src.solvers.pulp_solver import Status


class ExtractAnswerCommand(Command):
    """Command for extracting the answer from the solver's results."""

    def __init__(self, solver: str = 'solver', target: str = 'answer'):
        """Initialize an ExtractAnswerCommand instance.

        Args:
            solver (str): The attribute in the problem containing the solver.
            target (str): The attribute name in the problem where the answer will be stored.
        """
        super().__init__()
        self.solver = solver
        self.target = target
        self.inputs: list[KeyType] = [
            KeyType(self.solver, str)
        ]

        self.outputs: list[KeyType] = [
            KeyType(self.target, Answer)
        ]

    # pylint: disable=loop-invariant-statement
    def work(self, problem: Problem) -> None:
        """Extract the answer from the solver's results and stores it in the problem.

        If the solver's status is not optimal, the command will not store an answer.

        Args:
            problem (Problem): The problem instance from which to extract the answer.

        Raises:
            CommandException: If no solver is set.
        """
        if problem[self.solver] is None:
            raise CommandException("No solver has been set.")

        if problem[self.solver].status != Status.OPTIMAL:
            return

        problem[self.target] = Answer(problem[self.solver].board)
        for row in problem[self.solver].board.row_range:
            for column in problem[self.solver].board.column_range:
                problem[self.target].set_value(row, column, int(problem[self.solver].values[row][column].varValue))
