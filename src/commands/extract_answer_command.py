"""ExtractAnswerCommand."""
from src.commands.command import Command, CommandException
from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.solvers.answer import Answer
from src.solvers.pulp_solver import Status


class ExtractAnswerCommand(Command):
    """Command for extracting the data from the solver's results."""

    def __init__(self, solver: str = 'solver', target: str = 'answer'):
        """Initialize an ExtractAnswerCommand instance.

        Args:
            solver (str): The attribute in the problem containing the solver.
            target (str): The attribute name in the problem where the data will be stored.
        """
        super().__init__()
        self.solver = solver
        self.target = target
        self.inputs: list[KeyType] = [
            KeyType(self.solver, str),
        ]

        self.outputs: list[KeyType] = [
            KeyType(self.target, Answer),
        ]

    def work(self, problem: Problem) -> None:
        """Extract the data from the solver's results and store it in the problem.

        If the solver's status is not optimal, the command will not store any data.

        Args:
            problem (Problem): The problem instance from which to extract the data.

        Raises:
            CommandException: If no solver is set.
        """
        solver = problem.get(self.solver)

        if solver is None:
            raise CommandException('No solver has been set.')

        if solver.status != Status.OPTIMAL:
            return

        board = solver.board
        problem[self.target] = Answer(board)

        for row in board.row_range:
            for column in board.column_range:
                solver_choice = solver.choices[row][column]
                problem[self.target].set_value(row, column, int(solver_choice.varValue))
