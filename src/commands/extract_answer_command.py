"""ExtractAnswerCommand."""
from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.commands.solve_command import SolveCommand
from src.solvers.answer import Answer
from src.solvers.pulp_solver import Status


class ExtractAnswerCommand(SimpleCommand):
    """Command for extracting the line from the solver's results."""

    def __init__(self, solver: str = 'solver', target: str = 'answer'):
        """Initialize an ExtractAnswerCommand instance.

        Args:
            solver (str): The attribute in the problem containing the solver.
            target (str): The attribute name in the problem where the line will be stored.
        """
        super().__init__()
        self.add_preconditions([SolveCommand])
        self.target = 'answer'

    def work(self, problem: Problem) -> None:
        """Extract the line from the solver's results and store it in the problem.

        If the solver's status is not optimal, the command will not store any line.

        Args:
            problem (Problem): The problem instance from which to extract the line.

        Raises:
            CommandException: If no solver is set.
        """
        solver = problem.get(self.solver)

        if solver is None:
            raise CommandException('No solver has been set.')

        if solver.status != Status.OPTIMAL:
            return

        board = solver.board
        problem.answer = Answer(board)

        for row in board.row_range:
            for column in board.column_range:
                solver_choice = solver.variables.choices[row][column]
                problem.answer[row, column] = int(solver_choice.varValue)
